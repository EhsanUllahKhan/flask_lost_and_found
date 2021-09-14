#!/usr/bin/env bash

echo "*************** initializing celery worker ****************"

celery -A Backend.common.celery_app worker --loglevel=info