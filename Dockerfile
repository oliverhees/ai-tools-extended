# Use Python 3.11 as base image
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    python-multipart \
    yt-dlp \
    openai-whisper \
    pydub \
    requests \
    python-dotenv

# Copy application files
COPY main.py /app/
COPY youtube_extension.py /app/extensions/
COPY start_extended.sh /app/
RUN chmod +x /app/start_extended.sh

# Create necessary directories
RUN mkdir -p /app/media /app/cache /tmp

# Expose ports
EXPOSE 8000 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Start the application
CMD ["/app/start_extended.sh"]