from fastapi import APIRouter, HTTPException, Depends

from app.core.database import db_dependency
from app.core.security import get_current_user
from app.schema.task import CreateTask, UpdateTask
from app.models.task import Task
from app.services.task.create_service import create_service

task_router = APIRouter(prefix='/tasks', tags=['tasks'])

@task_router.post('/create')
async def create_task(db: db_dependency, create_task: CreateTask, get_user: dict = Depends(get_current_user)):
    task = create_service(get_user, create_task, db)

    return task

@task_router.get('/')
async def show_tasks(db: db_dependency, get_user: dict = Depends(get_current_user)):
    tasks = db.query(Task).filter(Task.user_id == get_user['user_id']).all()

    return tasks

@task_router.get('/{task_id}')
async def get_task(task_id: int, db: db_dependency, get_user: dict = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    if task.user_id == get_user['user_id']:
        return task
    else:
        raise HTTPException(status_code=401)
    
@task_router.put('/update/{task_id}')
async def update_task(task_id: int, db: db_dependency, update_task: UpdateTask, get_user: dict = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id).first()
    
    if task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    if task.user_id == get_user['user_id']:
        if update_task.name is not None: task.name = update_task.name
        if update_task.description is not None: task.description = update_task.description
        if update_task.done is not None: task.done = update_task.done

        db.commit()
        db.refresh(task)

        return task
    else:
        raise HTTPException(status_code=401)
    
@task_router.delete('/delete/{task_id}')
async def delete_task(task_id: int, db: db_dependency, get_user: dict = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id).first()
    
    if task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    if task.user_id == get_user['user_id']:
        db.delete(task)
        db.commit()

        return { 'status': 'deleted' }
