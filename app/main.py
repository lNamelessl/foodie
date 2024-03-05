from fastapi import FastAPI
from .routers import food, order, user, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/")
def say_hello():
    return "Hello, Everything works"


app.include_router(food.router)
app.include_router(order.router)
app.include_router(user.router)
app.include_router(auth.router)


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
