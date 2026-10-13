import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Pull database credentials from environment variables
DB_USER = os.getenv("MYSQL_USER", "AlternAssist_user")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
DB_HOST = os.getenv("MYSQL_HOST", "db")
DB_NAME = os.getenv("MYSQL_DATABASE", "AlternAssist_db")
DB_PORT = os.getenv("MYSQL_PORT", "3306")

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Session factory for handling database transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency to inject DB sessions into FastAPI path operations
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()