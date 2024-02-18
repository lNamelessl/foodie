from fastapi import APIRouter, HTTPException, status, Response, Depends
from app import schemas, models, oauth2
from sqlalchemy.orm import Session
from app.database import get_db
from typing import List
from app.models import Orders
from sqlalchemy import func, Update


router = APIRouter(tags=["Order"])


# Adds all the price columns and returns the total
@router.get("/total", status_code=status.HTTP_202_ACCEPTED)
def total_cost(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
):
    total = (
        db.query(func.sum(models.Orders.price))
        .filter(
            models.Orders.owner_id == current_user.id, models.Orders.payment == False
        )
        .all()
    )
    total = total[0][0]
    if total == None:
        total = 0
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="You haven't placed any order"
        )
    total = {"total": int(f"{total}")}
    return total


# Returns the orders that are in cart
@router.get("/cart", status_code=status.HTTP_202_ACCEPTED)
def checkout(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
):
    orders_query = db.query(models.Orders).filter(
        models.Orders.owner_id == current_user.id, models.Orders.payment == False
    )
    orders = orders_query.all()
    total = total_cost(db=db, current_user=current_user)
    return orders


# Creates a new order, stores it in the db and returns a response
@router.post(
    "/main",
    status_code=status.HTTP_201_CREATED,
)
def order_main_dish(
    user_order: schemas.Order,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    order = (
        db.query(models.MainDish).filter(models.MainDish.id == user_order.id).first()
    )
    if not order:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"meal with {user_order} doesn't exist"
        )
    price = order.price
    new_order = models.Orders(
        owner_id=current_user.id, order_id=order.id, food=order.main_dish, price=price
    )
    db.add(new_order)
    db.commit()
    total = total_cost(db=db, current_user=current_user)
    return {
        "Message": f"You've successfully placed your order 🙂, [subtotal: ₦{total['total']}]
    "}


# Creates a new order, stores it in the db and returns a response
@router.post(
    "/side",
    status_code=status.HTTP_201_CREATED,
)
def order_side_dish(
    user_order: schemas.Order,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    order = (
        db.query(models.SideDish).filter(models.SideDish.id == user_order.id).first()
    )
    if not order:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="meal doesn't exist")
    price = order.price
    new_order = models.Orders(
        owner_id=current_user.id, order_id=order.id, food=order.side_dish, price=price
    )
    db.add(new_order)
    db.commit()
    total = total_cost(db=db, current_user=current_user)
    return {
        "Message": f"You've successfully placed your order 🙂, [subtotal: ₦{total['total']}]
    "}


# # Creates a new order, stores it in the db and returns a response
@router.post(
    "/desert",
    status_code=status.HTTP_201_CREATED,
)
def order_desert(
    order: schemas.Order,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    order = db.query(models.Desert).filter(models.Desert.id == order.id).first()
    if not order:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="meal doesn't exist")
    price = order.price
    new_order = models.Orders(
        owner_id=current_user.id, order_id=order.id, food=order.desert, price=price
    )
    total = total_cost(db=db, current_user=current_user)
    db.add(new_order)
    db.commit()
    return {
        "Message": f"You've successfully placed your order 🙂, [subtotal: ₦{total['total']}]
    "}


# Creates a new order, stores it in the db and returns a response
@router.post("/drinks", status_code=status.HTTP_201_CREATED)
def order_drinks(
    order: schemas.Order,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    order = db.query(models.Drinks).filter(models.Drinks.id == order.id).first()
    if not order:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="meal doesn't exist")
    price = order.price
    new_order = models.Orders(
        owner_id=current_user.id, order_id=order.id, food=order.drinks, price=price
    )
    total = total_cost(db=db, current_user=current_user)
    db.add(new_order)
    db.commit()
    return {
        "Message": f"You've successfully placed your order 🙂, [subtotal: ₦{total['total']}]
    "
}

# Deletes a selected order
@router.delete("/delete_order")
def delete_order(
    order: schemas.Order,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    query = db.query(models.Orders).filter(models.Orders.id == order.id)
    order = query.first()
    if order == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"order does not exist 🙂
        ")
    if order.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="not authorised to perform this action 😑")
    query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Takes users payment and finalises order
@router.put(
    "/checkout",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=List[schemas.CheckOut],
)
def payment(
    payment: schemas.Payment,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    total = total_cost(db=db, current_user=current_user)
    payment = payment.model_dump()
    payment = payment["payment"]
    total = total["total"]
    if total > payment:
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail="Not enough amount of money 😏")
    elif total < payment:
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail="Too much amount of money 🙄")
    orders_query = db.query(models.Orders).filter(
        models.Orders.owner_id == current_user.id, models.Orders.payment == True
    )
    updated_payment = (
        Update(Orders).where(Orders.owner_id == current_user.id).values(payment=True)
    )
    db.execute(updated_payment)
    db.commit()
    return orders_query.all()
