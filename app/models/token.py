from app.core.database import Base

from sqlalchemy import Column, Integer, String, DateTime

class Token(Base):
    __tablename__ = 'tokens'

    id = Column(Integer, primary_key=True, index=True)
    access_token = Column(String, unique=True)
    token_type = Column(String, default='Bearer')
    expires = Column(DateTime)