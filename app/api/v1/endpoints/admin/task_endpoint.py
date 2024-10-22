from fastapi import APIRouter, Depends, HTTPException

from app.core.database import db_dependency
from app.core.security import get_current_user
from app.models.task import Task
from app.models.user import UserRole, User
from app.schema.task import UpdateTask, AdminCreateTask
from app.services.admin.task.update_service import update_service

task_router = APIRouter(prefix='/tasks')

@task_router.get('/')
async def show_tasks(db: db_dependency, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()

    if current_admin.role == UserRole.admin:
        tasks = db.query(Task).all()

        return tasks
    
@task_router.put('/update/{task_id}')
async def update_task(task_id: int, db: db_dependency, update_task: UpdateTask, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()
    
    task = update_service(current_admin, task_id, update_task, db)

    return task

@task_router.delete('/delete/{task_id}')
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
    
@task_router.get('/{task_id}')
async def show_task(task_id: int, db: db_dependency, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()
    task = db.query(Task).filter(Task.id == task_id).first()

    if current_admin.role == UserRole.admin:
        return task
    else:
        raise HTTPException(status_code=401, detail='Could not validate')

@task_router.post('/create')
async def create_task(db: db_dependency, create_task: AdminCreateTask, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()

    if current_admin.role == UserRole.admin:
        create_task_model = Task(
            name = create_task.name,
            description = create_task.description,
            user_id = create_task.user_id
        )

        db.add(create_task_model)
        db.commit()

        return { 'status': 'created' }
    else:
        raise HTTPException(status_code=401, detail='Could not validate')
 
    
    