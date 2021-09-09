from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship

from ..db import Base


class Item(Base):
    __tablename__ = "items"

    lost_item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=50))
    lost_date = Column(Date)
    is_found=Column(Boolean)
    lost_by_user_id = Column(Integer, ForeignKey("user.user_id"))
    lost_by_user = relationship("User", foreign_keys=[lost_by_user_id])

    found_by_user_id = Column(Integer, ForeignKey("user.user_id"), nullable=True)
    found_by_user = relationship("User", foreign_keys=[found_by_user_id])