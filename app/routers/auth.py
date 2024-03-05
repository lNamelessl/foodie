from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import database, schemas, models, utils, oauth2


router = APIRouter(tags=["Authentication"])


@router.post("/login")
def login(user_credentials: schemas.UserLogin, db: Session = Depends(database.get_db)):
    """_summary_:This function logs in a user

    Args:
    user_credentials: schemas.UserLogin: The user's credentials
    db (Session): The database session

    Raises:
        HTTPException[404]: Raises an exception if user is not found
        HTTPException[403]: Raises an exception if the credentials are not valid

    Returns:
        str: The access token
    """
    user = (
        db.query(models.User)
        .filter(models.User.email == user_credentials.email)
        .first()
    )
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials"
        )

    access_token = oauth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
