from pyclbr import Class
from typing import Optional
from pydantic  import BaseModel, EmailStr, conint
from datetime import datetime

class Order(BaseModel):
    id:int

class UserOut(BaseModel):
    id:int
    email:EmailStr

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserLogin(UserCreate):
    pass

class TokenData(Order):
    pass

class CheckOut(BaseModel):
    id:int
    food: str
    price: int
    created_at:datetime
    payment:bool
  
class TotalCost(BaseModel):
    total:int

class Payment(BaseModel):
    payment:int


