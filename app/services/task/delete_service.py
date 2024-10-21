from fastapi import HTTPException

from app.models.task import Task

def delete_service(task_id, get_user, db):
    task = db.query(Task).filter(Task.id == task_id).first()
    
    if task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    if task.user_id == get_user['user_id']:
        db.delete(task)
        db.commit()
    else:
        raise HTTPException(status_code=401, detail='Could not validate')