from fastapi import HTTPException

from app.models.team import Team
from app.models.user import UserRole

def update_service(current_admin, team_id, update_team, db):
    team = db.query(Team).filter(Team.id == team_id).first()

    if team is None:
        raise HTTPException(status_code=404, detail='Could not find team')
    if current_admin.role == UserRole.admin:
        if update_team.name is not None: 
            team.name = update_team.name
        if update_team.department_id is not None: 
            team.department_id = update_team.department_id
        if update_team.team_leader is not None: 
            team.team_leader = update_team.team_leader

        db.commit()
        db.refresh(team)

        return team
    raise HTTPException(status_code=401, detail='Could not validate')