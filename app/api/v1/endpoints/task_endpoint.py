from fastapi import APIRouter, HTTPException, Depends

from starlette import status

from typing import List

from app.core.database import db_dependency
from app.core.security import get_current_user
from app.schema.task import CreateTask, UpdateTask
from app.models.task import Task
from app.services.task.update_service import update_service
from app.services.task.create_service import create_service
from app.services.task.delete_service import delete_service
from app.serializers.task_serializer import TaskSerializer

task_router = APIRouter(prefix='/tasks', tags=['tasks'])

@task_router.post('/create', status_code=status.HTTP_201_CREATED, response_model=TaskSerializer)
async def create_task(db: db_dependency, create_task: CreateTask, get_user: dict = Depends(get_current_user)):
    task = create_service(get_user, create_task, db)

    return task

@task_router.get('/', response_model=List[TaskSerializer])
async def show_tasks(db: db_dependency, get_user: dict = Depends(get_current_user)):
    tasks = db.query(Task).filter(Task.user_id == get_user['user_id']).all()

    return tasks

@task_router.get('/{task_id}', response_model=TaskSerializer)
async def get_task(task_id: int, db: db_dependency, get_user: dict = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    if task.user_id == get_user['user_id']:
        return task
    else:
        raise HTTPException(status_code=401)
    
@task_router.put('/update/{task_id}', response_model=TaskSerializer)
async def update_task(task_id: int, db: db_dependency, update_task: UpdateTask, get_user: dict = Depends(get_current_user)):
    task = update_service(task_id, get_user, update_task, db)

    return task
    
@task_router.delete('/delete/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, db: db_dependency, get_user: dict = Depends(get_current_user)):
    delete_service(task_id, get_user, db)
