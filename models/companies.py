from sqlalchemy import Column, Integer, String, ForeignKey
from db.base import Base

class User(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    website = Column(String)
    notes = Column(Integer)