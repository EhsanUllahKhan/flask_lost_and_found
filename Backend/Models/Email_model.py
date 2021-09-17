from sqlalchemy import Column, Integer, String, Text

from ..db import Base


class Email(Base):
    ID_KEY = "email_id"
    SENDER_EMAIL = "sender_email"
    RECEIVER_EMAIL = "receiver_email"
    SUBJECT = "subject"
    MESSAGE = "message"

    __tablename__ = "emails"

    email_id = Column(Integer, primary_key=True, nullable=False)
    sender_email = Column(String(length=100), nullable=False)
    receiver_email = Column(String(length=100), nullable=False)
    subject = Column(String(length=100), nullable=False)
    message = Column(Text)

    def __init__(self, sender_email, receiver_email, subject, message):
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.subject = subject
        self.message = message

    def to_json(self):
        return {
            self.ID_KEY: self.email_id,
            self.SENDER_EMAIL: self.sender_email,
            self.RECEIVER_EMAIL: self.receiver_email,
            self.SUBJECT: self.subject,
            self.MESSAGE: self.message
        }
