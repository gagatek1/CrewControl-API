from fastapi import HTTPException

from app.models.department import Department
from app.models.user import UserRole

def update_service(current_admin, department_id, update_department, db):
    department = db.query(Department).filter(Department.id == department_id).first()

    if not department:
        raise HTTPException(status_code=404, detail='Could not find department')
    if current_admin.role == UserRole.admin:
        department.name = update_department.name

        db.commit()
        db.refresh(department)

        return department
    else:
        raise HTTPException(status_code=401, detail='Could not validate')
