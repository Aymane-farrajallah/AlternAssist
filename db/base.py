from sqlalchemy import Column, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Options appliquées à chaque table MySQL
MYSQL_TABLE_ARGS = {"mysql_engine": "InnoDB", "mysql_charset": "utf8mb4"}


class TimestampMixin:
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )