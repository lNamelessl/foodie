from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.sql.expression import null, text
from .database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship


class MainDish(Base):
    __tablename__ = "main_dish"

    main_dish = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)


class SideDish(Base):
    __tablename__ = "side_dish"

    side_dish = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)


class Desert(Base):
    __tablename__ = "desert"

    desert = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)


class Drinks(Base):
    __tablename__ = "drinks"

    drinks = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    phone_number = Column(String, nullable=True)
    orders = Column(String, nullable=False, unique=True)
    orders = relationship("Orders", back_populates="owner")


class Orders(Base):
    __tablename__ = "orders"

    food = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    owner_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    order_id = Column(Integer, primary_key=True, nullable=False)
    owner = relationship("User", back_populates="orders")
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    payment = Column(Boolean, nullable=False, default=False)
