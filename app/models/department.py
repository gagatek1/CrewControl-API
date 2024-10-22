from app.core.database import Base

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Department(Base):
    __tablename__ = 'departments'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    teams = relationship('Team', back_populates='department')
