from fastapi import FastAPI,APIRouter,HTTPException,status,Response,Depends
from app import schemas,models,oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List


orders = []

app = FastAPI()
router = APIRouter(prefix="/order", tags=["Order"])

@router.post("/main",status_code=status.HTTP_201_CREATED,)
def order_main_dish(order:schemas.Order, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    order = db.query(models.MainDish).filter(models.MainDish.id == order.id).first()
    orders.append(order)
    if not order:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="meal doesn't exist")
    return order
    
@router.post("/side",status_code=status.HTTP_201_CREATED,)
def order_side_dish(order:schemas.Order, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    order = db.query(models.SideDish).filter(models.MainDish.id == order.id).first()
    if not order:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="meal doesn't exist")
    return order
    
@router.post("/desert",status_code=status.HTTP_201_CREATED,)
def order_desert(order:schemas.Order, db: Session = Depends(get_db)):
    order = db.query(models.Desert).filter(models.MainDish.id == order.id).first()
    if not order:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="meal doesn't exist")
    return order

@router.post("/drinks",status_code=status.HTTP_201_CREATED,)
def order_drinks(order:schemas.Order, db: Session = Depends(get_db)):
    order = db.query(models.Drinks).filter(models.MainDish.id == order.id).first()
    if not order:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="meal doesn't exist")
    return order
#track user orders, calculate amount and checkout

