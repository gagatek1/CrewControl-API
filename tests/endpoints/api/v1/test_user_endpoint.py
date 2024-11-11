from fastapi.testclient import TestClient

from faker import Faker

from main import app

client = TestClient(app)

fake = Faker()

def test_user_create_endpoint():
    username = fake.user_name()
    email = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    response = client.post(
        '/api/v1/users/create',
        json = {
            'username': username,
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'password': fake.password()
        }  
    )
    
    assert response.status_code == 201
