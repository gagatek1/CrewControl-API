from fastapi import HTTPException

from app.models.department import Department
from app.models.user import UserRole

def create_service(current_admin, create_department, db):
    if current_admin.role == UserRole.admin:
        create_department_model = Department(
            name = create_department.name
        )

        db.add(create_department_model)
        db.commit()
        db.refresh(create_department_model)

        return create_department_model
    else:
        raise HTTPException(status_code=401, detail='Could not validate')
