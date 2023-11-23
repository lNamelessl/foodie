from fastapi import FastAPI,APIRouter,HTTPException,status,Response,Depends
from app import schemas,models,oauth2
from sqlalchemy.orm import Session
from app.database import get_db
from typing import List
from pydantic import BaseModel, Field
from app.models import Orders
from sqlalchemy import func


total = 0

app = FastAPI()
router = APIRouter(prefix="/order", tags=["Order"])

@router.post("/main",status_code=status.HTTP_201_CREATED,)
def order_main_dish(user_order:schemas.Order, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    
    order = db.query(models.MainDish).filter(models.MainDish.id == user_order.id).first()
    price = order.price
    if not user_order:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="meal doesn't exist")
    new_order = models.Orders(owner_id=current_user.id,order_id=order.id,food=order.main_dish,price=price)
    
    
    
    db.add(new_order)
    db.commit()
    total = total_cost(db=db)
    
    return f"message:" "You've successfully placed your order,"  f" (subtotal: ₦{total['total']})"
    
@router.post("/side",status_code=status.HTTP_201_CREATED,)
def order_side_dish(order:schemas.Order, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    order = db.query(models.SideDish).filter(models.SideDish.id == order.id).first()
   
    if not order:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="meal doesn't exist")
    new_order = models.Orders(owner_id=current_user.id,order_id=order.id,food=order.side_dish,price=price)
    
    db.add(new_order)
    db.commit()
    price = order.price
    total = total_cost(price)
   
    return f"message:" "You've successfully placed your order,"  f" (subtotal: ₦{total})"
    
@router.post("/desert",status_code=status.HTTP_201_CREATED,)
def order_desert(order:schemas.Order, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    global total
    order = db.query(models.Desert).filter(models.Desert.id == order.id).first()
    price = order.price
    if not order:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="meal doesn't exist")
    new_order = models.Orders(owner_id=current_user.id,order_id=order.id,food=order.desert,price=price)
    
    total_costs = total_cost(price)
    db.add(new_order)
    db.commit()
    
    return f"message:" "You've successfully placed your order,"  f" (subtotal: ₦{total})"
    

@router.post("/drinks",status_code=status.HTTP_201_CREATED,)
def order_drinks(order:schemas.Order, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    global total
    order = db.query(models.Drinks).filter(models.Drinks.id == order.id).first()
    price = order.price
    if not order:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="meal doesn't exist")
    new_order = models.Orders(owner_id=current_user.id,order_id=order.id,food=order.drinks,price=price)
    total_costs = total_cost()
    db.add(new_order)
    db.commit()
    
    return f"message:" "You've successfully placed your order,"  f" (subtotal: ₦{total})"


    

@router.get("/checkout")
def checkout(db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    orders_query = db.query(models.Orders).filter(models.Orders.owner_id==current_user.id)
    orders = orders_query.all()
    total = total_cost(db=db)
    return total

    

@router.delete("/delete_order",)
def delete_order(order: schemas.Order, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    query = db.query(models.Orders).filter(models.Orders.id == order.id)
    order = query.first()
    if order == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"order does not exist")
    if order.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="not authorised to perform this action")
    query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# def total_cost(price):
#     global total
#     total += price
#     return total
 
@router.get("/t",)
def total_cost(db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    total = db.query(func.sum(models.Orders.price)).all()
    total = total[0][0]
    if total == None:
        total = 0
    total  = {"total": int(f"{total}")}
   
    return total


@router.put("/payment",)
def payment(payment:schemas.Payment, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    total = total_cost(db=db)
    payment= payment.model_dump()
    payment = payment["payment"]
    total = total["total"]
    if total == payment:
        order_query = db.query(models.Orders)
        order = models.Orders(payment=True)
        # order = {"payment":True}
        order_query.update(order,synchronize_session=False)
        db.commit()
        return  order_query.first()
        return {"You've successfully placed your order"}


# track user orders, calculate amount and checkout

