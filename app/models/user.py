from core.database import Base, engine
from sqlalchemy import Column, Integer, String, Enum
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
    

Base.metadata.create_all(bind=engine)