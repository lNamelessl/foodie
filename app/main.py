from fastapi import FastAPI, Depends
from .database import get_db
from sqlalchemy.orm import Session
from . import models
from .routers import food,order,user
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
@app.get("/")
def say_hello():
  return "Hello World"





# origins = ["*"]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(food.router)
app.include_router(order.router)
app.include_router(user.router)
