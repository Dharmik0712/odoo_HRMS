from uuid import uuid4
from sqlalchemy import Column, Numeric, ForeignKey, Date
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class Payroll(Base):
    __tablename__ = "payroll"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    basic_salary = Column(Numeric(10, 2), nullable=False)
    hra = Column(Numeric(10, 2), nullable=False)
    allowances = Column(Numeric(10, 2), nullable=False)
    deductions = Column(Numeric(10, 2), nullable=False)

    effective_from = Column(Date, nullable=False)
