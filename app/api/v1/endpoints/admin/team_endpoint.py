from fastapi import APIRouter, Depends

from starlette import status

from app.models.user import User
from app.schemas.team import UpdateTeam
from app.core.database import db_dependency
from app.core.security import get_current_user
from app.services.admin.team.update_service import update_service
from app.services.admin.team.delete_service import delete_service
from app.serializers.team_serializer import TeamSerializer

team_router = APIRouter(prefix='/teams')

@team_router.put('/update/{team_id}', response_model=TeamSerializer)
async def update_team(team_id: int, db: db_dependency, update_team: UpdateTeam, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()
    team = update_service(current_admin, team_id, update_team, db)

    return team

@team_router.delete('/delete/{team_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_team(team_id: int, db: db_dependency, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()

    delete_service(current_admin, team_id, db)
