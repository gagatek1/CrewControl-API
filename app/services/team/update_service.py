from fastapi import HTTPException

from app.models.team import Team

def update_service(team_id, update_team, get_user, db):
    team = db.query(Team).filter(Team.id == team_id).first()
    user_id = get_user['user_id']

    if team is None:
        raise HTTPException(status_code=404, detail='Could not find team')
    if team.team_leader == user_id:
        if update_team.name is not None:
            team.name = update_team.name

        if update_team.department is not None:
            team.department = update_team.department

        if update_team.team_leader is not None:
            team.team_leader = update_team.team_leader

        db.commit()
        db.refresh(team)

        return team
    raise HTTPException(status_code=401)
