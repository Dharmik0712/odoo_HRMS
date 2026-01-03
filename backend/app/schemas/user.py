from pydantic import BaseModel, EmailStr
from app.models.user import UserRole


class UserResponse(BaseModel):
    id: str
    employee_id: str
    email: EmailStr
    role: UserRole
    is_active: bool

    class Config:
        from_attributes = True
