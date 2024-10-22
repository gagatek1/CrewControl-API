from fastapi import APIRouter, Depends, HTTPException

from app.models.team import Team
from app.models.user import User, UserRole
from app.schema.team import UpdateTeam
from app.core.database import db_dependency
from app.core.security import get_current_user
from app.services.admin.team.update_service import update_service

team_router = APIRouter(prefix='/teams')

@team_router.put('/update/{team_id}')
async def update_team(team_id: int, db: db_dependency, update_team: UpdateTeam, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()
    team = update_service(current_admin, team_id, update_team, db)

    return team

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
