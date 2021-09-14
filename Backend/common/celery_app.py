import os
from celery import Celery

CELERY_BROKER_URL = os.getenv("REDIS_SERVER", "redis://redis_server:6379")
CELERY_RESULT_BACKEND = os.getenv("REDIS_SERVER", "redis://redis_server:6379")

celery = Celery(
    "celery",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND,
    include=['Backend.tasks.celery_app']
)
