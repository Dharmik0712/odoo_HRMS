from sqlalchemy.orm import Session

from app.models.payroll import Payroll
from app.repositories.payroll_repo import PayrollRepository
from app.core.exceptions import ForbiddenException
from app.core.logging import logger
from app.models.user import UserRole


class PayrollService:

    def __init__(self):
        self.repo = PayrollRepository()

    def my_payroll(self, db: Session, user):
        return self.repo.get_by_user(db, user.id)

    def all_payroll(self, db: Session, user):
        if user.role != UserRole.ADMIN:
            raise ForbiddenException("Admin access required")
        return self.repo.get_all(db)

    def create_or_update(self, db: Session, user, employee_id, payload):
        if user.role != UserRole.ADMIN:
            raise ForbiddenException("Admin access required")

        payroll = Payroll(
            user_id=employee_id,
            basic_salary=payload.basic_salary,
            hra=payload.hra,
            allowances=payload.allowances,
            deductions=payload.deductions,
            effective_from=payload.effective_from,
        )

        try:
            self.repo.create(db, payroll)
            logger.info(
                "payroll_updated",
                employee_id=str(employee_id),
                admin_id=str(user.id),
            )
            return payroll
        except Exception as e:
            logger.exception("payroll_update_failed", error=str(e))
            raise
