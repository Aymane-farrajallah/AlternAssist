from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from db.base import Base

class User(Base):
    __tablename__ = "agent_runs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    tool_calls = Column(Integer)
    prompt_tokens = Column(Integer)
    completion_tokens = Column(Integer)
    created_at = Column(DateTime)