from fastapi import HTTPException

from app.models.user import User, UserRole

def delete_service(current_admin, user_id, db):
    user = db.query(User).filter(User.id == user_id).first()

    if current_admin.role == UserRole.admin:
        if not user:
            raise HTTPException(status_code=404, detail='Could not find user')
        db.delete(user)
        db.commit()
    else:
        raise HTTPException(status_code=401, detail='Could not validate')