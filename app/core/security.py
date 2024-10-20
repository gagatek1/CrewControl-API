from datetime import timedelta, datetime, timezone

from jose import jwt

from dotenv import load_dotenv

from app.models.token import Token

import os

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = 'HS256'

def create_access_token(username: str, user_id: int, expires_delta: timedelta, db):
    encode = {'sub': username, 'id': user_id}
    expires_date = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires_date})

    token_model = Token(
        access_token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM),
        expires = expires_date
    )

    db.add(token_model)
    db.commit()

    token = db.query(Token).filter(Token.access_token == token_model.access_token).first()

    return token
