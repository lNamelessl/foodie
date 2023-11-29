from ast import mod
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException,status
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app import database, models
from app.models import User
from . import schemas
from .config import settings
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

# Creates access token
def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

# Verifies access token
def verify_access_token(token: str):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id:int = payload.get("user_id")
        token_data = schemas.TokenData(id=id)
    except JWTError:
         raise HTTPException(status.HTTP_401_UNAUTHORIZED
         )
    return token_data

# Returns current user
def get_current_user(token:str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    token = verify_access_token(token)
    user = db.query(models.User).filter_by(id=token.id).first()
    return user
