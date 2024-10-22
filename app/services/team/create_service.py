from fastapi import HTTPException

from app.models.user import User
from app.models.team import Team
from app.models.department import Department

def create_service(get_user, create_team, db):
    user = db.query(User).filter(User.id == get_user['user_id']).first()
    department = db.query(Department).filter(Department.id == create_team.department_id).first()

    if not department:
        raise HTTPException(status_code=404, detail='Could not find department')

    create_team_model = Team(
        name=create_team.name,
        department_id=create_team.department_id,
        team_leader=user.id
    )

    db.add(create_team_model)
    db.commit()
    db.refresh(create_team_model)

    return create_team_model
    