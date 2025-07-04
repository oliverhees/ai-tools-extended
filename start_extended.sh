#!/bin/bash

# Start the YouTube extension service in background
cd /app/extensions
python3 youtube_extension.py &

# Start the original AI Tools service
# Assuming the base image has an entrypoint script
cd /app
if [ -f "/app/start.sh" ]; then
    exec /app/start.sh
elif [ -f "/app/main.py" ]; then
    exec python3 /app/main.py
else
    # If we can't find the main script, just keep the container running
    echo "AI Tools Extended is running..."
    echo "Original API: http://localhost:8000"
    echo "YouTube Extension: http://localhost:8080"
    tail -f /dev/null
fi