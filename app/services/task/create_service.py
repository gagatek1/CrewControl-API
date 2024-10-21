from app.models.user import User
from app.models.task import Task

def create_service(get_user, create_task, db):
    user = db.query(User).filter(User.id == get_user['user_id']).first()

    
    create_task_model = Task(
        name = create_task.name,
        description = create_task.description,
        user_id = user.id
    )
 
    db.add(create_task_model)
    db.commit()
    db.refresh(create_task_model)

    return create_task_model