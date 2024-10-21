from app.core.database import Base

from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from enum import Enum as PyEnum


class UserRole(PyEnum):
    admin = 'admin'
    user = 'user'

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, index=True, unique=True)
    username = Column(String, unique=True)
    role = Column(Enum(UserRole), default=UserRole.user)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    team_id = Column(Integer, ForeignKey('teams.id'), default=None)
    tasks = relationship('Task', back_populates='user')
    team = relationship('Team', back_populates='users')
    
