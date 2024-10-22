from fastapi import HTTPException

from app.models.user import UserRole
from app.models.task import Task



def update_service(current_admin, task_id, update_task, db):
    if current_admin.role == UserRole.admin:
        task = db.query(Task).filter(Task.id == task_id).first()
    else:
        raise HTTPException(status_code=401, detail='Could not validate')
    
    if task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    if update_task.name is not None: 
        task.name = update_task.name
    if update_task.description is not None: 
        task.description = update_task.description
    if update_task.done is not None: 
        task.done = update_task.done

    db.commit()
    db.refresh(task)

    return task
