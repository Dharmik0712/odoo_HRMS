from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import decode_token, oauth2_scheme
from app.repositories.user_repo import UserRepository
from app.db.session import SessionLocal
from app.core.exceptions import UnauthorizedException

router = APIRouter()
repo = UserRepository()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    payload = decode_token(token)
    user = repo.get_by_id(db, payload.get("sub"))
    if not user:
        raise UnauthorizedException()
    return user


@router.get("/me")
def me(current_user=Depends(get_current_user)):
    return current_user
