from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repo import UserRepository
from app.schemas.auth import SignupRequest, LoginRequest
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)
from app.core.exceptions import BadRequestException, UnauthorizedException
from app.core.logging import logger


class AuthService:

    def __init__(self):
        self.repo = UserRepository()

    def signup(self, db: Session, payload: SignupRequest):
        if self.repo.get_by_email(db, payload.email):
            raise BadRequestException("Email already registered")

        user = User(
            employee_id=payload.employee_id,
            email=payload.email,
            hashed_password=hash_password(payload.password),
            role=payload.role,
        )

        try:
            self.repo.create(db, user)
            logger.info("user_registered", email=payload.email)
            return user
        except Exception as e:
            logger.exception("signup_failed", error=str(e))
            raise

    def login(self, db: Session, payload: LoginRequest):
        user = self.repo.get_by_email(db, payload.email)

        if not user or not verify_password(
            payload.password, user.hashed_password
        ):
            raise UnauthorizedException("Invalid credentials")

        token = create_access_token(
            {"sub": str(user.id), "role": user.role}
        )

        logger.info("user_logged_in", email=user.email)
        return token
