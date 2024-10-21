from fastapi import APIRouter, Depends

from app.models.team import Team
from app.models.user import User
from app.schema.team import CreateTeam
from app.core.database import db_dependency
from app.core.security import get_current_user

team_router = APIRouter(prefix='/teams', tags=['teams'])

@team_router.post('/create')
async def create_team(db: db_dependency, create_team: CreateTeam, get_user: dict = Depends(get_current_user)):
    user = db.query(User).filter(User.id == get_user['user_id']).first()

    create_team_model = Team(
        name=create_team.name,
        department=create_team.department,
        team_leader=user.id
    )

    db.add(create_team_model)
    db.commit()

    return { 'status': 'created' }

@team_router.get('/')
async def show_teams(db: db_dependency, get_user: dict = Depends(get_current_user)):
    teams = db.query(Team).all()

    return teams

