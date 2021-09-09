from sqlalchemy import Column, String, Integer


from ..db import Base


class User(Base):      #db.Model
    EMAIL_KEY = "email"

    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    email = Column(String(80), unique=True)

    def __init__(self, email):
        self.email = email

    def to_json(self):
        return {
            self.EMAIL_KEY: self.email,
        }

