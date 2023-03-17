from fastapi import FastAPI, HTTPException, status
from schema import Orders
from database import Base,engine, SessionLocal
import model

Base.metadata.create_all(engine)
db = SessionLocal()

app = FastAPI()
# OrderAPI

@app.get("/orders",response_model=list[Orders])     #To view all data from database to user
def get_all_orders():
    orders = db.query(model.Orders).all()

    return orders

@app.get("/order/{order_id}")       #To view a single record from database to user
def get_by_id(order_id:int):
    # filter is used for conditions
    order = db.query(model.Orders).filter(model.Orders.orderID==order_id).first() 
    if order is None:       #if given order_id is not exist it will raise error else return order.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    return order

@app.post("/order",                             # it will take data from user and store in database
          status_code=status.HTTP_201_CREATED)  # HTTP_201_CREATED to show that new recorded is stored
def create_order(order:Orders):                 # here we are accepting the complete data
    new_order = model.Orders(
        productName=order.productName,
        productPrice=order.productPrice,
        purchaseByName=order.purchaseByName,
        purchaseDate=order.purchaseDate
    )
    db.add(new_order)                           # add the data into table.
    db.commit()                                 #commit() is used to commit the current transaction
    return new_order
#delete a single order using order_id
@app.delete('/order/{order_id}')
def delete_item(order_id:int):
    order_to_delete=db.query(model.Orders).filter(model.Orders.orderID==order_id).first()

    if order_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(order_to_delete)
    db.commit()

    return order_to_delete


