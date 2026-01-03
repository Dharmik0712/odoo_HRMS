import enum
from uuid import uuid4
from sqlalchemy import Column, Date, DateTime, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class AttendanceStatus(str, enum.Enum):
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"
    HALF_DAY = "HALF_DAY"
    LEAVE = "LEAVE"


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    date = Column(Date, nullable=False)
    check_in = Column(DateTime, nullable=True)
    check_out = Column(DateTime, nullable=True)
    status = Column(Enum(AttendanceStatus), nullable=False)
