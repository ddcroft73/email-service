#!/bin/bash
set -e

# load the .env variables
export $(grep -v '^#' .env | xargs)

#start the server and the app...
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# start celery...