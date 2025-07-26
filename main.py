#!/usr/bin/env python3
"""
AI Tools Extended - Main FastAPI Application
Unified API for AI Tools, YouTube processing, and N8N workflows
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import uvicorn
import os
import subprocess
import threading
import time

app = FastAPI(
    title="AI Tools Extended",
    description="Unified API for AI-powered content creation with YouTube integration",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "AI Tools Extended - Community Edition",
        "version": "1.0.0",
        "endpoints": {
            "api": "/api/*",
            "youtube": "/youtube/*", 
            "workflows": "/workflows/*",
            "docs": "/docs"
        }
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "services": {
            "ai_tools": "running",
            "youtube_api": "running", 
            "nginx": "ready"
        }
    }

@app.get("/api/")
async def api_info():
    return {
        "message": "AI Tools API",
        "endpoints": [
            "/api/text-to-speech",
            "/api/speech-to-text", 
            "/api/upload",
            "/api/download/{file_id}",
            "/api/generate-captioned-video"
        ]
    }

@app.get("/youtube/")
async def youtube_info():
    return {
        "message": "YouTube Extension API", 
        "endpoints": [
            "/youtube/transcribe",
            "/youtube/to-tts",
            "/youtube/to-captioned-video",
            "/youtube/extract-thumbnail"
        ]
    }

def start_youtube_service():
    """Start YouTube extension service on port 8080"""
    try:
        subprocess.run([
            "python3", "/app/extensions/youtube_extension.py"
        ], check=True)
    except Exception as e:
        print(f"Error starting YouTube service: {e}")

if __name__ == "__main__":
    # Start YouTube service in background
    youtube_thread = threading.Thread(target=start_youtube_service, daemon=True)
    youtube_thread.start()
    
    # Give services time to start
    time.sleep(2)
    
    # Start main API
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000,
        log_level="info"
    )