import enum
from uuid import uuid4
from sqlalchemy import Column, Date, Enum, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class LeaveType(str, enum.Enum):
    PAID = "PAID"
    SICK = "SICK"
    UNPAID = "UNPAID"


class LeaveStatus(str, enum.Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


class LeaveRequest(Base):
    __tablename__ = "leave_requests"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    leave_type = Column(Enum(LeaveType), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    status = Column(Enum(LeaveStatus), default=LeaveStatus.PENDING)
    remarks = Column(Text, nullable=True)
    admin_comment = Column(Text, nullable=True)
