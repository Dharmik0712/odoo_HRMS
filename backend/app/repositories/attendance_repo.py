from datetime import date
from sqlalchemy.orm import Session
from app.models.attendance import Attendance


class AttendanceRepository:

    def get_by_user_and_date(
        self, db: Session, user_id, attendance_date: date
    ):
        return (
            db.query(Attendance)
            .filter(
                Attendance.user_id == user_id,
                Attendance.date == attendance_date,
            )
            .first()
        )

    def get_by_user(self, db: Session, user_id):
        return (
            db.query(Attendance)
            .filter(Attendance.user_id == user_id)
            .order_by(Attendance.date.desc())
            .all()
        )

    def get_all(self, db: Session):
        return db.query(Attendance).order_by(Attendance.date.desc()).all()

    def save(self, db: Session, attendance: Attendance):
        db.add(attendance)
        db.commit()
        db.refresh(attendance)
        return attendance
