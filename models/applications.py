from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Index
from db.base import Base, MYSQL_TABLE_ARGS, TimestampMixin


class Applications(TimestampMixin, Base):
    __tablename__ = "applications"
    __table_args__ = (
        Index("ix_applications_user_status", "user_id", "status"),
        MYSQL_TABLE_ARGS,
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    offer_id = Column(Integer, ForeignKey("job_offers.id"), nullable=False)
    status = Column(String(50), nullable=False)
    applied_at = Column(DateTime)
    notes = Column(Text)