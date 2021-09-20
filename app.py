from flask_sqlalchemy import SQLAlchemy
from Backend import create_app

# from flask_mail import Mail

app = create_app()
db = SQLAlchemy(app)
app.app_context().push()
# mail = Mail(app)

@app.route('/')
def hello_world():
    return "Helooooooooooooooo"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
