from datetime import date, datetime

from sqlalchemy.orm import Session

from app.models.attendance import Attendance, AttendanceStatus
from app.repositories.attendance_repo import AttendanceRepository
from app.core.exceptions import BadRequestException
from app.core.logging import logger


class AttendanceService:

    def __init__(self):
        self.repo = AttendanceRepository()

    def check_in(self, db: Session, user):
        today = date.today()

        existing = self.repo.get_by_user_and_date(db, user.id, today)
        if existing and existing.check_in:
            raise BadRequestException("Already checked in today")

        attendance = existing or Attendance(
            user_id=user.id,
            date=today,
            status=AttendanceStatus.PRESENT,
        )

        attendance.check_in = datetime.utcnow()

        try:
            self.repo.save(db, attendance)
            logger.info(
                "attendance_check_in",
                user_id=str(user.id),
                date=str(today),
            )
            return attendance
        except Exception as e:
            logger.exception("check_in_failed", error=str(e))
            raise

    def check_out(self, db: Session, user):
        today = date.today()
        attendance = self.repo.get_by_user_and_date(db, user.id, today)

        if not attendance or not attendance.check_in:
            raise BadRequestException("Check-in required before check-out")

        if attendance.check_out:
            raise BadRequestException("Already checked out today")

        attendance.check_out = datetime.utcnow()

        try:
            self.repo.save(db, attendance)
            logger.info(
                "attendance_check_out",
                user_id=str(user.id),
                date=str(today),
            )
            return attendance
        except Exception as e:
            logger.exception("check_out_failed", error=str(e))
            raise

    def view_my_attendance(self, db: Session, user):
        return self.repo.get_by_user(db, user.id)

    def view_all_attendance(self, db: Session):
        return self.repo.get_all(db)
