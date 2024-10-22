from passlib.context import CryptContext

from app.models.user import User

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def create_service(db, create_user):
    create_user_model = User(
            email=create_user.email,
            username=create_user.username,
            first_name=create_user.first_name,
            last_name=create_user.last_name,
            hashed_password=bcrypt_context.hash(create_user.password)
        )

    db.add(create_user_model)
    db.commit()
    db.refresh(create_user_model)

    return create_user_model
