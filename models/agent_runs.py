from sqlalchemy import Column, Integer, ForeignKey
from db.base import Base, MYSQL_TABLE_ARGS, TimestampMixin


class Agent_Runs(TimestampMixin, Base):
    __tablename__ = "agent_runs"
    __table_args__ = MYSQL_TABLE_ARGS

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    tool_calls = Column(Integer)
    prompt_tokens = Column(Integer)
    completion_tokens = Column(Integer)