from fastapi import HTTPException

from app.models.user import UserRole
from app.models.task import Task


def delete_service(current_admin, task_id, db):
    task = db.query(Task).filter(Task.id == task_id).first()

    if current_admin.role == UserRole.admin:
        if not task:
            raise HTTPException(status_code=404, detail='Could not find task')
        db.delete(task)
        db.commit()
    else:
        raise HTTPException(status_code=401, detail='Could not validate')
