#!/bin/bash
set -e

celery -A celery_app worker --loglevel=info --logfile=logs/celery.log