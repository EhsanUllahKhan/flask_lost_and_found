from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Backend import create_app
from Backend.User import User as user_routes
# from Backend.Item import Item as item_routes

app = create_app()
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@db:3306/flask_db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return "Helooooooooooooooo"


# app.register_blueprint(user_routes)
# app.register_blueprint(item_routes)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
