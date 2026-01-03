from sqlalchemy.orm import Session
from datetime import timedelta

from app.models.leave import LeaveRequest, LeaveStatus
from app.repositories.leave_repo import LeaveRepository
from app.core.exceptions import BadRequestException, ForbiddenException
from app.core.logging import logger
from app.models.user import UserRole


class LeaveService:

    def __init__(self):
        self.repo = LeaveRepository()

    def apply_leave(self, db: Session, user, payload):
        if payload.start_date > payload.end_date:
            raise BadRequestException("Start date cannot be after end date")

        leave = LeaveRequest(
            user_id=user.id,
            leave_type=payload.leave_type,
            start_date=payload.start_date,
            end_date=payload.end_date,
            remarks=payload.remarks,
            status=LeaveStatus.PENDING,
        )

        try:
            self.repo.create(db, leave)
            logger.info(
                "leave_applied",
                user_id=str(user.id),
                leave_id=str(leave.id),
            )
            return leave
        except Exception as e:
            logger.exception("leave_apply_failed", error=str(e))
            raise

    def my_leaves(self, db: Session, user):
        return self.repo.get_by_user(db, user.id)

    def all_leaves(self, db: Session, user):
        if user.role != UserRole.ADMIN:
            raise ForbiddenException("Admin access required")
        return self.repo.get_all(db)

    def decide_leave(self, db: Session, user, leave_id, payload):
        if user.role != UserRole.ADMIN:
            raise ForbiddenException("Admin access required")

        leave = self.repo.get_by_id(db, leave_id)
        if not leave:
            raise BadRequestException("Leave request not found")

        if leave.status != LeaveStatus.PENDING:
            raise BadRequestException("Leave already processed")

        leave.status = (
            LeaveStatus.APPROVED if payload.approve else LeaveStatus.REJECTED
        )
        leave.admin_comment = payload.admin_comment

        try:
            self.repo.save(db, leave)
            logger.info(
                "leave_decision",
                leave_id=str(leave.id),
                status=leave.status,
                admin_id=str(user.id),
            )
            return leave
        except Exception as e:
            logger.exception("leave_decision_failed", error=str(e))
            raise
