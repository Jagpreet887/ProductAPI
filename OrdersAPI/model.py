#The models data classes define the sql tables

from database import Base
from datetime import date
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
class Orders(Base):
    __tablename__ = "Orders"
    orderID =Column(Integer, primary_key=True)
    productName = Column(String)
    productPrice = Column(Integer)
    purchaseByName = Column(String)
    purchaseDate =Column(Date, index=True)

class Profile(Base):
    __tablename__ = "Profile"
    profileID = Column(Integer, primary_key=True) 
    profileName = Column(String)
    profilePictureURL = Column(String )