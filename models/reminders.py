from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from db.base import Base

class User(Base):
    __tablename__ = "reminders"
    id = Column(Integer, primary_key=True , autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    application_id = Column(Integer, ForeignKey('applications.id'))
    due_date = Column(DateTime)
    done = Column(Boolean)
    message_draft = Column(String)