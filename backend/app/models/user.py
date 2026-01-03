import enum
from uuid import uuid4
from sqlalchemy import Column, String, Boolean, Enum
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class UserRole(str, enum.Enum):
    EMPLOYEE = "EMPLOYEE"
    ADMIN = "ADMIN"


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    employee_id = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    is_active = Column(Boolean, default=True)

