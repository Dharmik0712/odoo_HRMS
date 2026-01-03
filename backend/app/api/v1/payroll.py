from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.payroll import PayrollCreateRequest, PayrollResponse
from app.services.payroll_service import PayrollService
from app.api.v1.users import get_current_user
from app.db.session import SessionLocal

router = APIRouter()
service = PayrollService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/me", response_model=PayrollResponse | None)
def my_payroll(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.my_payroll(db, current_user)


@router.get("/all", response_model=list[PayrollResponse])
def all_payroll(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.all_payroll(db, current_user)


@router.post("/{employee_id}", response_model=PayrollResponse)
def update_payroll(
    employee_id: str,
    payload: PayrollCreateRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.create_or_update(
        db, current_user, employee_id, payload
    )
