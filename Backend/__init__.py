import os
from flask_mail import Mail
from flask import Flask

mail = Mail()


def create_app():
    app = Flask(__name__)

    app.config['MAIL_DEFAULT_SENDER'] = 'ehsanullah@wanclouds.net'

    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@db:3306/flask_db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")

    mail.init_app(app)

    from Backend.User import User as user_routes
    from Backend.Item import Item as item_routes
    from Backend.tasks import Task as task_routes
    from Backend.Email import Email as email_routes

    app.register_blueprint(user_routes)
    app.register_blueprint(item_routes)
    app.register_blueprint(task_routes)
    app.register_blueprint(email_routes)

    return app
