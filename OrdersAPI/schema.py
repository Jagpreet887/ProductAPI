#the schemas data classes define the api that FastAPI uses to interact with the database

from pydantic import BaseModel
from datetime import date

class Orders(BaseModel):
    orderID : int
    productName : str
    productPrice : float
    purchaseByName : str
    purchaseDate : date

    class Config:
        orm_mode=True

class Profile(BaseModel):
    profileID : int 
    profileName : str 
    profilePictureURL : str

    class Config:
        orm_mode=True