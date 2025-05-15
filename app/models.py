from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class SpoofedLog(Base):
    __tablename__ = "spoofed_logs"

    id = Column(Integer, primary_key=True)
    domain = Column(String)
    src_ip = Column(String)
    ttl = Column(Integer)
    length = Column(Integer)
    timestamp = Column(TIMESTAMP, default=datetime.utcnow)
