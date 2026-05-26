from passlib.context import CryptContext
from jose import jwt
from datetime import datetime,timedelta
from dotenv import load_dotenv
import os
from jose import JWTError
from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import get_db
from models.model import User
load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password:str):
    return pwd_context.hash(password)


def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)


def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=1)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,
                             SECRET_KEY,
                             algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token:str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        email = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code = 401,
                detail = "Invalid Token"
            )
        return {
            "email":email,
            "role":payload.get("role")
        }
    except JWTError:
        raise HTTPException(
            status_code = 401,
            detail = "Invalid or expired Token"
        )


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Token"
            )

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid or Expired Token"
        )

    user = db.query(User).filter(
        User.email == email
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=403,
            detail="Account Disabled"
        )

    if not user.is_verified:
        raise HTTPException(
            status_code=403,
            detail="Email Not Verified"
        )

    return user


def admin_only(current_user:User=Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code = 403,
            detail = "Admin Access Required"
        )
    return current_user

def manager_only(current_user:User=Depends(get_current_user)):
    if current_user.role != "manager":
        raise HTTPException(
            status_code = 403,
            detail ="Manager Access Required"
        )
    return current_user

def employee_only(current_user:User=Depends(get_current_user)):
    if current_user.role != "employee":
        raise HTTPException(
            status_code = 403,
            detail = "Employee Access Required"
        )
    return current_user

