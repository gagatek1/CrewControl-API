from fastapi import HTTPException

from app.models.team import Team
from app.models.department import Department

def update_service(team_id, update_team, get_user, db):
    team = db.query(Team).filter(Team.id == team_id).first()
    department = db.query(Department).filter(Department.id == update_team.department_id).first()
    user_id = get_user['user_id']

    if not team:
        raise HTTPException(status_code=404, detail='Could not find team')
    if not department:
        raise HTTPException(status_code=404, detail='Could not find department')
    if team.team_leader == user_id:
        if update_team.name is not None:
            team.name = update_team.name

        if update_team.department_id is not None:
            team.department_id = update_team.department_id

        if update_team.team_leader is not None:
            team.team_leader = update_team.team_leader

        db.commit()
        db.refresh(team)

        return team
    raise HTTPException(status_code=401)
