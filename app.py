from flask_sqlalchemy import SQLAlchemy
from Backend import create_app
from Backend import Models
from flask_mail import Mail

app = create_app()
db = SQLAlchemy(app)
# mail = Mail(app)

@app.route('/')
def hello_world():
    return "Helooooooooooooooo"

def make_shell_context():
    return dict(app=app, db=db, models=Models)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
