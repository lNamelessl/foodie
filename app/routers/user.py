from fastapi import APIRouter,HTTPException,status,Response,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..import models,schemas,utils
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/users",tags=["users"])

# Takes in users credentials and create a new user
@router.post("/" ,status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut )
def create_user(user: schemas.UserCreate,db: Session = Depends(get_db), ):
    if IntegrityError:
        raise HTTPException(status_code=status.HTTP_226_IM_USED,detail="User with that Email already exist😐")
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Returns user details
@router.get("/{id}",response_model=schemas.UserOut)
def get_user(id:int,db: Session = Depends(get_db),):
    user = db.query(models.User).filter(models.User.id == id).first()
     
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id {id} was not found")
    return user