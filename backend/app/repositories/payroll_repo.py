from sqlalchemy.orm import Session
from app.models.payroll import Payroll


class PayrollRepository:

    def create(self, db: Session, payroll: Payroll):
        db.add(payroll)
        db.commit()
        db.refresh(payroll)
        return payroll

    def get_by_user(self, db: Session, user_id):
        return (
            db.query(Payroll)
            .filter(Payroll.user_id == user_id)
            .order_by(Payroll.effective_from.desc())
            .first()
        )

    def get_all(self, db: Session):
        return (
            db.query(Payroll)
            .order_by(Payroll.effective_from.desc())
            .all()
        )
