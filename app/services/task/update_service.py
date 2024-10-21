from fastapi import HTTPException

from app.models.task import Task

def update_service(task_id, get_user, update_task, db):
    task = db.query(Task).filter(Task.id == task_id).first()
    
    if task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    if task.user_id == get_user['user_id']:
        if update_task.name is not None:
            task.name = update_task.name
            
        if update_task.description is not None: 
            task.description = update_task.description

        if update_task.done is not None: 
            task.done = update_task.done

        db.commit()
        db.refresh(task)

        return task
    else:
        raise HTTPException(status_code=401)