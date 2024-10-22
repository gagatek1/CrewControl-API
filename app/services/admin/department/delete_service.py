from fastapi import HTTPException

from app.models.department import Department
from app.models.user import UserRole

def delete_service(current_admin, department_id, db):
    department = db.query(Department).filter(Department.id == department_id).first()

    if not department:
        raise HTTPException(status_code=404, detail='Could not find department')
    
    if current_admin.role == UserRole.admin:
        db.delete(department)
        db.commit()
    else:
        raise HTTPException(status_code=401, detail='Could not validate')