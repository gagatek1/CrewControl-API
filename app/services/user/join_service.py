from fastapi import HTTPException

from app.models.user import User
from app.models.team import Team

def join_service(get_user, join_user, db):
    user = db.query(User).filter(User.id == get_user['user_id']).first()
    team = db.query(Team).filter(Team.id == join_user.team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail='Could not find team')
    
    user.team_id = join_user.team_id

    db.commit()
    db.refresh(user)

    return user
