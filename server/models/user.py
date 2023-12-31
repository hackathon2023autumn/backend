from sqlalchemy import Column, Integer, String
from server.models.base import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email=Column(String(64),unique=True,index=True)
    username = Column(String(64), index=True, nullable=False)
    password = Column(String(128))
    
