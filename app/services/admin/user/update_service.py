from fastapi import HTTPException

from app.models.user import UserRole, User

def update_service(current_admin, user_id, update_user, db):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail='Could not find user')

    if current_admin.role == UserRole.admin:
        if update_user.email is not None:
            user.email = update_user.email
        if update_user.username is not None:
            user.username = update_user.username
        if update_user.first_name is not None:
            user.first_name = update_user.first_name
        if update_user.last_name is not None:
            user.last_name = update_user.last_name
        user.role = update_user.role

        db.commit()
        db.refresh(user)

        return user
    else:
        raise HTTPException(status_code=401, detail='Could not validate')