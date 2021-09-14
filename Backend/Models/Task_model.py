from sqlalchemy import Column, Integer, String, Boolean

from ..db import Base


class Task(Base):
    ID_KEY = "task_id"
    TASK_TYPE = "task_type"
    TASK_STATUS = "task_status"
    TASK_RESULT = "task_result"
    MESSAGE = "message"

    __tablename__ = "tasks"

    # id= Column(Integer, primary_key=True, nullable=False)
    task_id = Column(String(100), primary_key=True, nullable=False)
    task_type = Column(String(length=100), nullable=False)
    task_status=Column(String(length=100), nullable=False)
    task_result = Column(String(length=100))
    message = Column(String(length=500))

    def __init__(self, task_id, task_type, task_status, task_result, message):
        self.task_id = task_id
        self.task_type = task_type
        self.task_status = task_status
        self.task_result = task_result
        self.message = message

    def to_json(self):
        return {
            self.ID_KEY: self.task_id,
            self.TASK_TYPE: self.task_type,
            self.TASK_STATUS: self.task_status,
            self.TASK_RESULT: self.task_result,
            self.MESSAGE : self.message
        }
