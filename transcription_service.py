from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import yt_dlp
import whisper
import tempfile
import os
import asyncio
from typing import Optional
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="YouTube Transcription API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Whisper model
model = whisper.load_model("base")

class TranscriptionRequest(BaseModel):
    url: str
    language: Optional[str] = None

class TranscriptionResponse(BaseModel):
    title: str
    duration: int
    transcription: str
    language: str

@app.get("/")
async def root():
    return {
        "service": "YouTube Transcription API",
        "version": "1.0.0",
        "endpoints": {
            "/transcribe": "POST - Transcribe YouTube video",
            "/health": "GET - Health check"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_video(request: TranscriptionRequest):
    """Transcribe a YouTube video using Whisper"""
    
    try:
        # Configure yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
            'outtmpl': tempfile.mktemp(suffix='.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        
        # Download video info and audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(request.url, download=True)
            audio_file = ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3')
            
            # Check video duration (max 10 minutes)
            duration = info.get('duration', 0)
            if duration > 600:
                os.remove(audio_file)
                raise HTTPException(
                    status_code=400,
                    detail="Video is too long. Maximum duration is 10 minutes."
                )
            
            title = info.get('title', 'Unknown')
        
        # Transcribe with Whisper
        logger.info(f"Transcribing {title}...")
        result = model.transcribe(
            audio_file,
            language=request.language,
            task="transcribe"
        )
        
        # Clean up
        os.remove(audio_file)
        
        return TranscriptionResponse(
            title=title,
            duration=duration,
            transcription=result["text"],
            language=result["language"]
        )
        
    except Exception as e:
        logger.error(f"Error transcribing video: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to transcribe video: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)