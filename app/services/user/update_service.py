from passlib.context import CryptContext

from app.models.user import User

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def update_service(update_user, get_user, db):
    user = db.query(User).filter(User.id == get_user['user_id']).first()
    
    if update_user.email is not None:
        user.email = update_user.email
    
    if update_user.username is not None:
        user.username = update_user.username
    
    if update_user.password is not None:
        user.hashed_password = bcrypt_context.hash(update_user.password)

    db.commit()
    db.refresh(user)

    return user
