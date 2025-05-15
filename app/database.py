from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

DATABASE_URL = "postgresql://postgres:Cse%4040668@localhost/dns_analyzer"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_engine():
    return engine

def init_db():
    Base.metadata.create_all(engine)
