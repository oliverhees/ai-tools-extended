# Extended AI Tools based on gyoridavid's image
FROM gyoridavid/ai-agents-no-code-tools:0.1.1

# Install additional dependencies for YouTube support
RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install yt-dlp for YouTube downloads
RUN pip3 install yt-dlp

# Create directory for custom scripts
WORKDIR /app/extensions

# Copy YouTube transcription extension
COPY youtube_extension.py .

# Keep the original working directory
WORKDIR /app

# Copy startup script that runs both services
COPY start_extended.sh /app/
RUN chmod +x /app/start_extended.sh

# The base image already exposes its ports, we just document them
# Port 8000 - Original AI Tools API
# Port 8080 - YouTube Extension API

EXPOSE 8080

# Override the CMD to run our extended startup
CMD ["/app/start_extended.sh"]