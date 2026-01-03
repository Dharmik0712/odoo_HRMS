from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings
from app.core.exceptions import UnauthorizedException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

ALGORITHM = "HS256"


from passlib.context import CryptContext
import hashlib

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)

def hash_password(password: str) -> str:
    sha256 = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return pwd_context.hash(sha256)

def verify_password(password: str, hashed: str) -> bool:
    sha256 = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return pwd_context.verify(sha256, hashed)



def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes=settings.access_token_expire_minutes
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.secret_key, algorithm=ALGORITHM)


def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
    except JWTError:
        raise UnauthorizedException("Invalid or expired token")
