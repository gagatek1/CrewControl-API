from fastapi import APIRouter, Depends, HTTPException

from app.models.team import Team
from app.schema.team import CreateTeam, UpdateTeam
from app.core.database import db_dependency
from app.core.security import get_current_user
from app.services.team.create_service import create_service
from app.services.team.update_service import update_service

team_router = APIRouter(prefix='/teams', tags=['teams'])

@team_router.post('/create')
async def create_team(db: db_dependency, create_team: CreateTeam, get_user: dict = Depends(get_current_user)):
    user = create_service(get_user, create_team, db)

    return user

@team_router.get('/')
async def show_teams(db: db_dependency, get_user: dict = Depends(get_current_user)):
    teams = db.query(Team).all()

    return teams

@team_router.get('/{team_id}')
async def get_team(team_id: int, db: db_dependency, get_user: dict = Depends(get_current_user)):
    team = db.query(Team).filter(Team.id == team_id).first()

    if team is None:
        raise HTTPException(status_code=404, detail='Could not find team')

    return team

@team_router.put('/update/{team_id}')
async def update_team(team_id: int, db: db_dependency, update_team: UpdateTeam, get_user: dict = Depends(get_current_user)):
    team = update_service(team_id, update_team, get_user, db)

    return team

@team_router.delete('/delete/{team_id}')
async def delete_team(team_id: int, db: db_dependency, get_user: dict = Depends(get_current_user)):
    team = db.query(Team).filter(Team.id == team_id).first()
    user_id = get_user['user_id']

    if team is None:
        raise HTTPException(status_code=404, detail='Could not find team')
    if team.team_leader == user_id:
        db.delete(team)
        db.commit()

        return { 'status': 'deleted' }
    
    raise HTTPException(status_code=401)
