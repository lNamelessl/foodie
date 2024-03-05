from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from .config import settings
from . import schemas
from app import database, models

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(data: dict):
    """This function creates an access token

    Args:
        data (dict): The user data

    Returns:
        jwt_token[str]: The access token
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str):
    """This function verifies the user access token

    Args:
        token (str): The access token

    Raises:
        HTTPException[401]: Unauthorised action

    Returns:
        dict[str]: The token data
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: int = payload.get("user_id")
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)
    return token_data


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)
):
    """This function gets the current user

    Args:
        token (str): The access token
        db (Session): The database session

    Returns:
        models.User: The user object
    """
    token = verify_access_token(token)
    user = db.query(models.User).filter_by(id=token.id).first()
    return user
