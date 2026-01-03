from app.db.session import engine
from app.db.base import Base

# Explicit imports (important)
from app.models.user import User
from app.models.attendance import Attendance
from app.models.leave import LeaveRequest
from app.models.payroll import Payroll


def init_db():
    Base.metadata.create_all(bind=engine)
