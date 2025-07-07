from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database import Base
from datetime import date
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username= Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    bio = Column(String, nullable=True)
    created_at = Column(DateTime, default=date.today())

    blogs = relationship("Blog", back_populates="author")

 

    