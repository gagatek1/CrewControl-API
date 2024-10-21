from fastapi import APIRouter, Depends, HTTPException

from app.models.team import Team
from app.models.user import User, UserRole
from app.schema.team import UpdateTeam
from app.core.database import db_dependency
from app.core.security import get_current_user

team_router = APIRouter(prefix='/teams')

@team_router.put('/update/{team_id}')
async def update_team(team_id: int, db: db_dependency, update_team: UpdateTeam, get_admin: dict = Depends(get_current_user)):
    team = db.query(Team).filter(Team.id == team_id).first()
    admin = db.query(User).filter(User.id == get_admin['user_id']).first()

    if team is None:
        raise HTTPException(status_code=404, detail='Could not find team')
    if admin.role == UserRole.admin:
        if update_team.name is not None: team.name = update_team.name
        if update_team.department is not None: team.department = update_team.department
        if update_team.team_leader is not None: team.team_leader = update_team.team_leader

        db.commit()
        db.refresh(team)

        return team
    raise HTTPException(status_code=401)

@team_router.delete('/delete/{team_id}')
async def delete_team(team_id: int, db: db_dependency, get_admin: dict = Depends(get_current_user)):
    team = db.query(Team).filter(Team.id == team_id).first()
    admin = db.query(User).filter(User.id == get_admin['user_id']).first()

    if team is None:
        raise HTTPException(status_code=404, detail='Could not find team')
    if admin.role == UserRole.admin:
        db.delete(team)
        db.commit()

        return { 'status': 'deleted' }
    
    raise HTTPException(status_code=401)
