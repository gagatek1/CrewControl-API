import pytest

import os

from dotenv import load_dotenv

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.core.database import Base

load_dotenv(os.path.join('app', '.env'))

DATABASE_URL = os.getenv('TEST_DATABASE_URL')

def check_if_db_exists(db_name):
    url = '/'.join(DATABASE_URL.split('/')[:-1])
    temp_engine = create_engine(url + '/postgres')

    with temp_engine.connect() as connection:
        result = connection.execute(text(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}';"))
        return result.fetchone() is not None
    
def create_database(db_name):
    url = '/'.join(DATABASE_URL.split('/')[:-1])
    temp_engine = create_engine(url + '/postgres')

    with temp_engine.connect().execution_options(isolation_level="AUTOCOMMIT") as connection:
        connection.execute(text(f"CREATE DATABASE {db_name};"))

db_name = DATABASE_URL.split('/')[-1]

if not check_if_db_exists(db_name):
    create_database(db_name)

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

def teardown():
    Base.metadata.drop_all(bind=engine)
 