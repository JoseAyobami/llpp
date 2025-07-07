from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Base
from datetime import date
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    created_at = Column(DateTime, default=date.today())
    author_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    author = relationship("User", back_populates="blogs")

    

