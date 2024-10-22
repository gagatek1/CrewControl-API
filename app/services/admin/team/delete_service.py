from fastapi import HTTPException

from app.models.team import Team
from app.models.user import UserRole

def delete_service(current_admin, team_id, db):
    team = db.query(Team).filter(Team.id == team_id).first()

    if team is None:
        raise HTTPException(status_code=404, detail='Could not find team')
    if current_admin.role == UserRole.admin:
        db.delete(team)
        db.commit()

        return { 'status': 'deleted' }
    
    raise HTTPException(status_code=401, detail='Could not valid')