from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.auth import SignupRequest, LoginRequest, TokenResponse
from app.schemas.user import UserResponse
from app.services.auth_service import AuthService
from app.db.session import SessionLocal

router = APIRouter()
service = AuthService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/signup", response_model=UserResponse)
def signup(payload: SignupRequest, db: Session = Depends(get_db)):
    return service.signup(db, payload)


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    token = service.login(db, payload)
    return TokenResponse(access_token=token)
