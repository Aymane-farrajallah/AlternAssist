from sqlalchemy import Column, Integer, String, ForeignKey, Text
from db.base import Base, MYSQL_TABLE_ARGS, TimestampMixin


class Companies(TimestampMixin, Base):
    __tablename__ = "companies"
    __table_args__ = MYSQL_TABLE_ARGS

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(255), nullable=False)
    website = Column(String(255))
    notes = Column(Text)