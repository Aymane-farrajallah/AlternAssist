from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from db.base import Base

class User(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    offer_id = Column(Integer, ForeignKey('offers.id'))
    status = Column(String)
    applied_at = Column(DateTime)
    notes = Column(Integer)