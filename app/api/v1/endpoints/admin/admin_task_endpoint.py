from fastapi import APIRouter, Depends, HTTPException

from app.core.database import db_dependency
from app.core.security import get_current_user
from app.models.task import Task
from app.models.user import UserRole, User
from app.schema.task import UpdateTask

admin_task_router = APIRouter(prefix='/tasks')

@admin_task_router.get('/')
async def show_tasks(db: db_dependency, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()

    if current_admin.role == UserRole.admin:
        tasks = db.query(Task).all()

        return tasks
    
@admin_task_router.put('/update/{task_id}')
async def update_task(task_id: int, db: db_dependency, update_task: UpdateTask, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()
    
    if current_admin.role == UserRole.admin:
        task = db.query(Task).filter(Task.id == task_id).first()
    else:
        raise HTTPException(status_code=401, detail='Could not validate')
    
    if task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    if update_task.name is not None: task.name = update_task.name
    if update_task.description is not None: task.description = update_task.description
    if update_task.done is not None: task.done = update_task.done

    db.commit()
    db.refresh(task)

    return task

@admin_task_router.delete('/delete/{task_id}')
async def delete_task(task_id: int, db: db_dependency, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()
    task = db.query(Task).filter(Task.id == task_id).first()

    if current_admin.role == UserRole.admin:
        if not task:
            raise HTTPException(status_code=404, detail='Could not find task')
        db.delete(task)
        db.commit()

        return { 'status': 'deleted' }
    else:
        raise HTTPException(status_code=401, detail='Could not validate')
    
@admin_task_router.get('/{task_id}')
async def show_task(task_id: int, db: db_dependency, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()
    task = db.query(Task).filter(Task.id == task_id).first()

    if current_admin.role == UserRole.admin:
        return task
    else:
        raise HTTPException(status_code=401, detail='Could not validate')
    