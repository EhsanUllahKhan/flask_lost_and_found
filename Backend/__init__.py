from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@db:3306/flask_db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # db.init_app(app)
    # db.app = app

    from Backend.User import User as user_routes
    from Backend.Item import Item as item_routes

    app.register_blueprint(user_routes)
    app.register_blueprint(item_routes)

    return app
