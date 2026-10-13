from sqlalchemy import Column, Integer, String
from db.base import Base, MYSQL_TABLE_ARGS, TimestampMixin


class User(TimestampMixin, Base):
    __tablename__ = "users"
    __table_args__ = MYSQL_TABLE_ARGS

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False, server_default="user")