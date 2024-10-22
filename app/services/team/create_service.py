from app.models.user import User
from app.models.team import Team

def create_service(get_user, create_team, db):
    user = db.query(User).filter(User.id == get_user['user_id']).first()

    create_team_model = Team(
        name=create_team.name,
        department=create_team.department,
        team_leader=user.id
    )

    db.add(create_team_model)
    db.commit()
    db.refresh(create_team_model)

    return create_team_model
    