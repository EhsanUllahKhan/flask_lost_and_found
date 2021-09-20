import os
class config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@db:3306/flask_db"
    RABBITPARAMS = {
        "RABBIT_ENV_RABBITMQ_USER": "guest",
        "RABBIT_ENV_RABBITMQ_PASSWORD": "guest",
    }

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')