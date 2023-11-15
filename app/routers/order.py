from fastapi import FastAPI,APIRouter,HTTPException,status,Response,Depends
from app import schemas,models,oauth2
from sqlalchemy.orm import Session
from app.database import get_db
from typing import List
from pydantic import BaseModel, Field,Json
import json


total = 0

app = FastAPI()
router = APIRouter(prefix="/order", tags=["Order"])

@router.post("/main",status_code=status.HTTP_201_CREATED,)
def order_main_dish(user_order:schemas.Order, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    order = db.query(models.MainDish).filter(models.MainDish.id == user_order.id).first()
    if not user_order:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="meal doesn't exist")
    new_order = models.Orders(owner_id=current_user.id,order_id=order.id)
    price = order.price
    total_costs = total_cost(price)
    print(order.id)
    db.add(new_order)
    db.commit()

    return f"You've successfully ordered {total}"
    
@router.post("/side",status_code=status.HTTP_201_CREATED,)
def order_side_dish(order:schemas.Order, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    global total
    order = db.query(models.SideDish).filter(models.SideDish.id == order.id).first()
    price = order.price
    if not order:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="meal doesn't exist")
    new_order = models.Orders(owner_id=current_user.id,order_id=order.id,food=order.side_dish,price=price)
    
    total_costs = total_cost(price)
    print(order.id)
    db.add(new_order)
    db.commit()
    
    return f"You've successfully ordered {total}"
    
@router.post("/desert",status_code=status.HTTP_201_CREATED,)
def order_desert(order:schemas.Order, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    order = db.query(models.Desert).filter(models.Desert.id == order.id).first()
    if not order:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="meal doesn't exist")
    new_order = models.Orders(owner_id=current_user.id,order_id=order.id)
    price = order.price
    total_costs = total_cost(price)
    print(order.id)
    db.add(new_order)
    db.commit()

    return f"You've successfully ordered {total}"

@router.post("/drinks",status_code=status.HTTP_201_CREATED,)
def order_drinks(order:schemas.Order, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    order = db.query(models.Drinks).filter(models.Drinks.id == order.id).first()
    if not order:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="meal doesn't exist")
    new_order = models.Orders(owner_id=current_user.id,order_id=order.id)
    price = order.price
    total_costs = total_cost(price)
    print(order.id)
    db.add(new_order)
    db.commit()

    return f"You've successfully ordered {total}"

@router.get("/checkout",response_model=List[schemas.Checkout])
def checkout(db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    orders = db.query(models.Orders).filter(models.Orders.owner_id==current_user.id).all()

    print (orders)
    return orders

def total_cost(price):
    global total
    total += price
    return total



#track user orders, calculate amount and checkout

