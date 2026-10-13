from sqlalchemy import Column, Integer, String, ForeignKey , DateTime
from db.base import Base

class User(Base):
    __tablename__ = "job_offers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))
    title = Column(String)
    url = Column(String)
    source = Column(String)
    location = Column(String)
    status = Column(String)
    published_at = Column(DateTime)