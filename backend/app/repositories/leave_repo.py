from sqlalchemy.orm import Session
from app.models.leave import LeaveRequest


class LeaveRepository:

    def create(self, db: Session, leave: LeaveRequest):
        db.add(leave)
        db.commit()
        db.refresh(leave)
        return leave

    def get_by_user(self, db: Session, user_id):
        return (
            db.query(LeaveRequest)
            .filter(LeaveRequest.user_id == user_id)
            .order_by(LeaveRequest.start_date.desc())
            .all()
        )

    def get_all(self, db: Session):
        return (
            db.query(LeaveRequest)
            .order_by(LeaveRequest.start_date.desc())
            .all()
        )

    def get_by_id(self, db: Session, leave_id):
        return (
            db.query(LeaveRequest)
            .filter(LeaveRequest.id == leave_id)
            .first()
        )

    def save(self, db: Session, leave: LeaveRequest):
        db.add(leave)
        db.commit()
        db.refresh(leave)
        return leave
