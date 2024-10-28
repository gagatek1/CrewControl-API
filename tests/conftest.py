import pytest

import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv(os.path.join('app', '.env'))

Base = declarative_base()

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

@pytest.fixture(scope='function')
def setup():
    Base.metadata.create_all(bind=engine)
 