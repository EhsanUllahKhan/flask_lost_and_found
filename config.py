import os
class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@db:3306/flask_db"
    RABBITPARAMS = {
        "RABBIT_ENV_RABBITMQ_USER": "guest",
        "RABBIT_ENV_RABBITMQ_PASSWORD": "guest",
    }
    REDIS_PARAMS = {
        "PORT": int(6379),
        "PASSWORD": "root",
        "HOST": "redis",
        "DB": os.environ.get("REDIS_DB"),
    }
    CELERY_RESULT_BACKEND = "redis://:{PASSWORD}@{HOST}:{PORT}/{DB}".format(
        **REDIS_PARAMS
    )
    CELERY_BROKER_URL = "amqp://{RABBIT_ENV_RABBITMQ_USER}:{RABBIT_ENV_RABBITMQ_PASSWORD}@rabbitmq:5672//".format(
        **RABBITPARAMS
    )