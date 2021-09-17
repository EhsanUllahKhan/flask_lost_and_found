import os
from flask_mail import Mail
from flask import Flask

mail = Mail()


def create_app():
    app = Flask(__name__)
    mail.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@db:3306/flask_db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from Backend.User import User as user_routes
    from Backend.Item import Item as item_routes
    from Backend.tasks import Task as task_routes
    from Backend.Email import Email as email_routes

    app.register_blueprint(user_routes)
    app.register_blueprint(item_routes)
    app.register_blueprint(task_routes)
    app.register_blueprint(email_routes)

    return app
