from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship

from ..db import Base


class Item(Base):
    ID_KEY= "lost_item_id"
    NAME_KEY = "name"
    LOST_DATE_KEY = "lost_date"
    IS_FOUND_KEY = "is_found"
    LOST_BY_USER_ID_KEY = "lost_by_user_id"
    FOUND_BY_USER_ID_KEY = "found_by_user_id"

    __tablename__ = "items"

    lost_item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=50))
    lost_date = Column(Date)
    is_found=Column(Boolean)
    lost_by_user_id = Column(Integer, ForeignKey("user.user_id"))
    lost_by_user = relationship("User", foreign_keys=[lost_by_user_id])

    found_by_user_id = Column(Integer, ForeignKey("user.user_id"), nullable=True)
    found_by_user = relationship("User", foreign_keys=[found_by_user_id])

    def __init__(self, name, lost_date, is_found, lost_by_user_id, found_by_user_id ):
        self.name = name
        self.lost_date = lost_date
        self.is_found = is_found
        self.lost_by_user_id = lost_by_user_id
        self.found_by_user_id = found_by_user_id

    def to_json(self):
        return {
            self.ID_KEY: self.lost_item_id,
            self.NAME_KEY: self.name,
            self.LOST_DATE_KEY: self.lost_date,
            self.IS_FOUND_KEY: self.is_found,
            self.LOST_BY_USER_ID_KEY: self.lost_by_user_id,
            self.FOUND_BY_USER_ID_KEY: self.found_by_user_id
        }
