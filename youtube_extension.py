from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
import yt_dlp
import os
import tempfile
import requests
from typing import Optional
import json

app = FastAPI(title="YouTube Extension for AI Tools")

# Base URL for the original AI Tools API
BASE_API_URL = "http://localhost:8000"

class YouTubeRequest(BaseModel):
    url: str
    language: Optional[str] = "en"

class VideoToCaptionedRequest(BaseModel):
    youtube_url: str
    style: Optional[str] = "minimal"  # minimal, bold, gradient
    music: Optional[bool] = True

class YouTubeToTTSRequest(BaseModel):
    youtube_url: str
    voice: Optional[str] = "en-US-JennyNeural"
    speed: Optional[float] = 1.0

@app.get("/")
async def root():
    return {
        "service": "YouTube Extension for AI Tools",
        "base_features": "Access all original features at port 8000",
        "youtube_endpoints": {
            "/youtube/transcribe": "Transcribe YouTube video using Whisper",
            "/youtube/to-tts": "Convert YouTube video to TTS audio",
            "/youtube/to-captioned-video": "Create captioned video from YouTube",
            "/youtube/extract-thumbnail": "Extract thumbnail from YouTube video"
        }
    }

@app.post("/youtube/transcribe")
async def youtube_transcribe(request: YouTubeRequest):
    """Download YouTube video and transcribe using the base Whisper API"""
    try:
        # Download audio from YouTube
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'outtmpl': tempfile.mktemp(suffix='.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(request.url, download=True)
            audio_file = ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3')
            
        # Upload to media storage
        with open(audio_file, 'rb') as f:
            files = {'file': f}
            upload_response = requests.post(f"{BASE_API_URL}/upload", files=files)
            media_id = upload_response.json()['file_id']
        
        # Transcribe using Whisper
        transcribe_response = requests.post(
            f"{BASE_API_URL}/speech-to-text",
            json={"file_id": media_id, "language": request.language}
        )
        
        # Clean up
        os.remove(audio_file)
        requests.delete(f"{BASE_API_URL}/delete/{media_id}")
        
        return {
            "title": info.get('title'),
            "duration": info.get('duration'),
            "transcription": transcribe_response.json()
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/youtube/to-tts")
async def youtube_to_tts(request: YouTubeToTTSRequest):
    """Convert YouTube video to TTS audio"""
    try:
        # First transcribe the video
        transcribe_result = await youtube_transcribe(
            YouTubeRequest(url=request.youtube_url)
        )
        
        # Convert to TTS
        tts_response = requests.post(
            f"{BASE_API_URL}/text-to-speech",
            json={
                "text": transcribe_result["transcription"]["text"],
                "voice": request.voice,
                "speed": request.speed
            }
        )
        
        return {
            "title": transcribe_result["title"],
            "tts_file_id": tts_response.json()["file_id"],
            "download_url": f"{BASE_API_URL}/download/{tts_response.json()['file_id']}"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/youtube/to-captioned-video")
async def youtube_to_captioned_video(request: VideoToCaptionedRequest):
    """Create a captioned video from YouTube thumbnail and transcription"""
    try:
        # Get video info
        ydl_opts = {'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(request.youtube_url, download=False)
            thumbnail_url = info.get('thumbnail')
            title = info.get('title')
        
        # Download thumbnail
        thumbnail_response = requests.get(thumbnail_url)
        temp_thumb = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
        temp_thumb.write(thumbnail_response.content)
        temp_thumb.close()
        
        # Upload thumbnail
        with open(temp_thumb.name, 'rb') as f:
            files = {'file': f}
            upload_response = requests.post(f"{BASE_API_URL}/upload", files=files)
            image_id = upload_response.json()['file_id']
        
        # Transcribe video
        transcribe_result = await youtube_transcribe(
            YouTubeRequest(url=request.youtube_url)
        )
        
        # Create captioned video
        caption_response = requests.post(
            f"{BASE_API_URL}/generate-captioned-video",
            json={
                "image_id": image_id,
                "text": transcribe_result["transcription"]["text"][:500],  # Limit text
                "style": request.style,
                "add_music": request.music
            }
        )
        
        # Clean up
        os.remove(temp_thumb.name)
        
        return {
            "title": title,
            "video_file_id": caption_response.json()["file_id"],
            "download_url": f"{BASE_API_URL}/download/{caption_response.json()['file_id']}"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/youtube/extract-thumbnail")
async def extract_youtube_thumbnail(request: YouTubeRequest):
    """Extract and store thumbnail from YouTube video"""
    try:
        ydl_opts = {'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(request.url, download=False)
            thumbnail_url = info.get('thumbnail')
            title = info.get('title')
        
        # Download and upload thumbnail
        thumbnail_response = requests.get(thumbnail_url)
        files = {'file': ('thumbnail.jpg', thumbnail_response.content, 'image/jpeg')}
        upload_response = requests.post(f"{BASE_API_URL}/upload", files=files)
        
        return {
            "title": title,
            "thumbnail_id": upload_response.json()['file_id'],
            "download_url": f"{BASE_API_URL}/download/{upload_response.json()['file_id']}"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)