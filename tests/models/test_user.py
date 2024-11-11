from fastapi.testclient import TestClient

from faker import Faker

from app.models.user import User, UserRole
from app.models.department import Department
from app.models.team import Team
from main import app
from tests.conftest import db

client = TestClient(app)

fake = Faker()

def test_create_user():
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

    assert user.id is not None

def test_user_team_relationship():
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

    department = Department(
        name=fake.company()
    )

    db.add(department)
    db.commit()
    db.refresh(department)

    team = Team(
        name=fake.name(),
        department_id=department.id,
        team_leader=user.id
    )

    db.add(team)
    db.commit()
    db.refresh(team)

    user.team_id = team.id

    db.commit()
    db.refresh(user)

    assert user.team_id == team.id
    assert user.team.name == team.name
