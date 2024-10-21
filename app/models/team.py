from app.core.database import Base

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    department = Column(String, index=True)
    team_leader = Column(Integer, nullable=False)
    users = relationship('User', back_populates='team')
