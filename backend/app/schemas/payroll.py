from datetime import date
from pydantic import BaseModel


class PayrollCreateRequest(BaseModel):
    basic_salary: float
    hra: float
    allowances: float
    deductions: float
    effective_from: date


class PayrollResponse(BaseModel):
    user_id: str
    basic_salary: float
    hra: float
    allowances: float
    deductions: float
    effective_from: date

    class Config:
        from_attributes = True
