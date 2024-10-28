from fastapi.testclient import TestClient

from faker import Faker

from app.models.token import Token
from main import app
from tests.conftest import db

client = TestClient(app)

fake = Faker()

def test_create_token():
    token = Token(
        access_token=fake.uuid4(),
        expires=fake.date_time()
    )

    db.add(token)
    db.commit()
    db.refresh(token)

    assert token is not None
