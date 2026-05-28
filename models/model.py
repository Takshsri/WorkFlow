from datetime import datetime

from sqlalchemy import  Column, Date, DateTime, ForeignKey,Integer,String,Boolean
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,index=True)
    email = Column(String,unique=True,index=True)
    role = Column(String)
    password = Column(String)
    is_active = Column(Boolean,default=True)
    is_verified = Column(Boolean,default=False)


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,index=True)
    description = Column(String)
    status = Column(String,default="TODO")
    priority = Column(String,default="medium")
    assigned_to = Column(
        Integer,
        ForeignKey("users.id")
    )
    created_by = Column(
        Integer,
        ForeignKey("users.id")
    )
    deadline = Column(Date)
    created_at = Column(DateTime,default=datetime.utcnow)
    updated_at = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)

