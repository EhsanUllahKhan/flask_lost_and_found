from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@db:3306/flask_db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # db.init_app(app)
    # db.app = app

    from Backend.User import User as user_routes
    from Backend.Item import Item as item_routes
    from Backend.tasks import Task as task_routes

    app.register_blueprint(user_routes)
    app.register_blueprint(item_routes)
    app.register_blueprint(task_routes)

    return app
