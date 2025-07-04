#!/bin/bash

# Start the transcription service in background
python3 /app/transcription_service.py &

# Start the original service (assuming it has an entrypoint)
# This will depend on what the base image runs
exec "$@"