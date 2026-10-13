from sqlalchemy import (
    Column, Integer, String, ForeignKey, DateTime, Index, UniqueConstraint,
)
from db.base import Base, MYSQL_TABLE_ARGS, TimestampMixin


class Job_Offers(TimestampMixin, Base):
    __tablename__ = "job_offers"
    __table_args__ = (
        UniqueConstraint("user_id", "url", name="uq_job_offers_user_url"),
        Index("ix_job_offers_user_status", "user_id", "status"),
        MYSQL_TABLE_ARGS,
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"))
    title = Column(String(255), nullable=False)
    url = Column(String(255), nullable=False)
    source = Column(String(255))
    location = Column(String(255))
    status = Column(String(50), nullable=False)
    published_at = Column(DateTime)