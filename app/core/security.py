from fastapi import HTTPException, Header

from datetime import timedelta, datetime, timezone

from typing import Optional

from jose import jwt, JWTError

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

async def get_current_user(authorization: Optional[str] = Header(None)):
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Could not validate")
    
    token = authorization.split(" ")[1]

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=401, detail='Could not validate')
        else:
            return {
                'user_id': user_id,
                'username': username
            }
    except JWTError:
        raise HTTPException(status_code=401, detail='Could not validate')
