from fastapi.testclient import TestClient

from faker import Faker

from app.models.department import Department
from main import app
from tests.conftest import db

client = TestClient(app)

fake = Faker()

def test_create_department():
    department = Department(
        name=fake.company()
    )

    db.add(department)
    db.commit()
    db.refresh(department)

    assert department is not None
