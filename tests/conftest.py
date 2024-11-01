import pytest

import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.database import Base

load_dotenv(os.path.join('app', '.env'))

DATABASE_URL = os.getenv('TEST_DATABASE_URL')

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush= False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db = SessionLocal()

@pytest.fixture(scope='function', autouse=True)
def setup():
    Base.metadata.create_all(bind=engine)
 