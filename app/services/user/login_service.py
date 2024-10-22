from passlib.context import CryptContext

from fastapi import HTTPException

from datetime import timedelta

from app.models.user import User
from app.core.security import create_access_token

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')    

def login_service(username: str, password: str, db):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(status_code=401, detail='Could not validate user')
    if not bcrypt_context.verify(password, user.hashed_password):
        raise HTTPException(status_code=401, detail='Could not validate user')
    else:
        return create_access_token(
            username=user.username,
            user_id=user.id,
            expires_delta=timedelta(days=2),
            db=db
            )