from fastapi import APIRouter
from fastapi import Depends

from app.core.database import db_dependency
from app.core.security import get_current_user
from app.schema.task import CreateTask
from app.models.task import Task
from app.models.user import User

task_router = APIRouter(prefix='/tasks', tags=['tasks'])

@task_router.post('/create')
async def create_task(db: db_dependency, create_task: CreateTask, get_user: dict = Depends(get_current_user)):
    user = db.query(User).filter(User.id == get_user['user_id']).first()

    
    create_task_model = Task(
        name = create_task.name,
        description = create_task.description,
        user_id = user.id
    )
 
    db.add(create_task_model)
    db.commit()