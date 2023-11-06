from fastapi import APIRouter
from fastapi import FastAPI, Depends
from ..database import get_db
from sqlalchemy.orm import Session
from app import models

app = FastAPI()

router = APIRouter(prefix="/foodie",tags=["food"])


@router.get("/maindish")
def get_main_dish(db: Session = Depends(get_db)):
  query = db.query(models.MainDish).all()
  return query

@router.get("/sidedish")
def get_side_dish(db: Session = Depends(get_db)):
  query = db.query(models.SideDish).all()
  return query

@router.get("/desert")
def get_desert(db: Session = Depends(get_db)):
  query = db.query(models.Desert).all()
  return query

@router.get("/drinks")
def get_drinks(db: Session = Depends(get_db)):
  query = db.query(models.Drinks).all()
  return query

