from sqlalchemy import (
    Column, Integer, DateTime, Boolean, ForeignKey, Text, Index, text,
)
from db.base import Base, MYSQL_TABLE_ARGS, TimestampMixin


class Reminder(TimestampMixin, Base):
    __tablename__ = "reminders"
    __table_args__ = (
        Index("ix_reminders_due_done", "due_date", "done"),
        MYSQL_TABLE_ARGS,
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    application_id = Column(
        Integer,
        ForeignKey("applications.id", ondelete="CASCADE"),
        nullable=False,
    )
    due_date = Column(DateTime, nullable=False)
    done = Column(Boolean, nullable=False, server_default=text("0"))
    message_draft = Column(Text)