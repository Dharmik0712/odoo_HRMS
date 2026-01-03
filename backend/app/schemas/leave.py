from datetime import date
from pydantic import BaseModel
from app.models.leave import LeaveType, LeaveStatus


class LeaveApplyRequest(BaseModel):
    leave_type: LeaveType
    start_date: date
    end_date: date
    remarks: str | None = None


class LeaveDecisionRequest(BaseModel):
    approve: bool
    admin_comment: str | None = None


class LeaveResponse(BaseModel):
    id: str
    user_id: str
    leave_type: LeaveType
    start_date: date
    end_date: date
    status: LeaveStatus
    remarks: str | None
    admin_comment: str | None

    class Config:
        from_attributes = True
