from fastapi import HTTPException

from app.models.team import Team

def delete_service(team_id, get_user, db):
    team = db.query(Team).filter(Team.id == team_id).first()
    user_id = get_user['user_id']

    if team is None:
        raise HTTPException(status_code=404, detail='Could not find team')
    if team.team_leader == user_id:
        db.delete(team)
        db.commit()
    else:
        raise HTTPException(status_code=401)
