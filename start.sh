#!/bin/bash
#set -e

# load the .env variables
#export $(grep -v '^#' .env | xargs)

#start the server and the app...
#uvicorn main:app --host 0.0.0.0 --port 8000 --reload

#sleep 3


#./start_celery.sh > /dev/null 2>&1 &

#!/bin/bash
set -e

stop_celery() {
  killall -9 celery
}

handle_signal() {
  stop_celery
  exit 0
}

# Load the .env variables
export $(grep -v '^#' .env | xargs)

# Start the server and the app
uvicorn main:app --host 0.0.0.0 --port 8000 --reload &

# Start Celery
./start_celery.sh > /dev/null 2>&1 &

trap handle_signal SIGINT

wait
