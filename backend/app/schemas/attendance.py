from datetime import date, datetime
from pydantic import BaseModel
from app.models.attendance import AttendanceStatus
from pydantic_settings import BaseSettings

class CheckInRequest(BaseModel):
    pass


class CheckOutRequest(BaseModel):
    pass


class AttendanceResponse(BaseModel):
    date: date
    check_in: datetime | None
    check_out: datetime | None
    status: AttendanceStatus

    class Config:
        from_attributes = True
