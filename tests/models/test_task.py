from fastapi.testclient import TestClient

from faker import Faker

from app.models.user import User, UserRole
from app.models.task import Task
from main import app
from tests.conftest import db

client = TestClient(app)

fake = Faker()

def test_create_task():
    user = User(
        email=fake.email(),
        username=fake.user_name(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        hashed_password=fake.password(),
        role=UserRole.user
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    task = Task(
        name=fake.file_name(),
        description='Fake description',
        user_id=user.id
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    assert task is not None
    assert task.user_id == user.id
