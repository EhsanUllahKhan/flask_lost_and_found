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
    MAIL_USERNAME = "ehsanullah@wanclouds.net"
    MAIL_PASSWORD = "comsatswah"
    MAIL_DEFAULT_SENDER = 'ehsanullah@wanclouds.net'