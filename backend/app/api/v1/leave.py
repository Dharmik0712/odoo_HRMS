from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.leave import (
    LeaveApplyRequest,
    LeaveDecisionRequest,
    LeaveResponse,
)
from app.services.leave_service import LeaveService
from app.api.v1.users import get_current_user
from app.db.session import SessionLocal

router = APIRouter()
service = LeaveService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/apply", response_model=LeaveResponse)
def apply_leave(
    payload: LeaveApplyRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.apply_leave(db, current_user, payload)


@router.get("/me", response_model=list[LeaveResponse])
def my_leaves(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.my_leaves(db, current_user)


@router.get("/all", response_model=list[LeaveResponse])
def all_leaves(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.all_leaves(db, current_user)


@router.post("/{leave_id}/decision", response_model=LeaveResponse)
def decide_leave(
    leave_id: str,
    payload: LeaveDecisionRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.decide_leave(db, current_user, leave_id, payload)
