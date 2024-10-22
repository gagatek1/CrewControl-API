from fastapi import HTTPException

from app.models.user import UserRole, User
from app.models.task import Task

def create_service(current_admin, create_task, db):
    user = db.query(User).filter(User.id == create_task.user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail='Could not find user')

    if current_admin.role == UserRole.admin:
        create_task_model = Task(
            name = create_task.name,
            description = create_task.description,
            user_id = create_task.user_id
        )

        db.add(create_task_model)
        db.commit()
        db.refresh(create_task_model)

        return create_task_model
        
    else:
        raise HTTPException(status_code=401, detail='Could not validate')
