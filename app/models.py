from sqlalchemy import Column, ForeignKey,Integer,String,Boolean
from sqlalchemy.sql.expression import null, text 
from .database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

class MainDish(Base):
    __tablename__ = "main_dish"

    main_dish = Column(String,nullable=False)
    price = Column(Integer,nullable=False)
    id = Column(Integer,primary_key=True,nullable=False)

class SideDish(Base):
    __tablename__ = "side_dish"

    side_dish = Column(String,nullable=False)
    price = Column(Integer,nullable=False)
    id = Column(Integer,primary_key=True,nullable=False)

class Desert(Base):
    __tablename__ = "desert"

    desert = Column(String,nullable=False)
    price = Column(Integer,nullable=False)
    id = Column(Integer,primary_key=True,nullable=False)

class Drinks(Base):
    __tablename__ = "drinks"

    drinks = Column(String,nullable=False)
    price = Column(Integer,nullable=False)
    id = Column(Integer,primary_key=True,nullable=False)