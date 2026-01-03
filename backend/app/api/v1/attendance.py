from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.attendance_service import AttendanceService
from app.schemas.attendance import AttendanceResponse
from app.api.v1.users import get_current_user
from app.db.session import SessionLocal
from app.core.exceptions import ForbiddenException
from app.models.user import UserRole

router = APIRouter()
service = AttendanceService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/check-in", response_model=AttendanceResponse)
def check_in(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.check_in(db, current_user)


@router.post("/check-out", response_model=AttendanceResponse)
def check_out(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.check_out(db, current_user)


@router.get("/me", response_model=list[AttendanceResponse])
def my_attendance(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.view_my_attendance(db, current_user)


@router.get("/all", response_model=list[AttendanceResponse])
def all_attendance(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if current_user.role != UserRole.ADMIN:
        raise ForbiddenException("Admin access required")

    return service.view_all_attendance(db)
