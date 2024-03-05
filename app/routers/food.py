from fastapi import APIRouter
from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session

from app import models
from ..database import get_db


router = APIRouter(prefix="/foodie", tags=["food"])


@router.get("/maindish", status_code=status.HTTP_300_MULTIPLE_CHOICES)
def get_main_dish(db: Session = Depends(get_db)):
    """This function displays the the list of main dishes

    Args:
        db (Session): The database session

    Returns:
        dict[str, Any]: Returns the list of main dishes
    """
    query = db.query(models.MainDish).all()
    return query


@router.get("/sidedish")
def get_side_dish(db: Session = Depends(get_db)):
    """This function displays the the list of side dishes

    Args:
        db (Session): The database session

    Returns:
        dict[str, Any]: Returns the list of side dishes
    """
    query = db.query(models.SideDish).all()
    return query


@router.get("/desert")
def get_desert(db: Session = Depends(get_db)):
    """This function displays the the list of deserts

    Args:
        db (Session): The database session

    Returns:
        dict[str, Any]: Returns the list of deserts
    """
    query = db.query(models.Desert).all()
    return query


@router.get("/drinks")
def get_drinks(db: Session = Depends(get_db)):
    """This function displays the the list of drinks

    Args:
        db (Session): The database session

    Returns:
        dict[str, Any]: Returns the list of drinks
    """
    query = db.query(models.Drinks).all()
    return query
