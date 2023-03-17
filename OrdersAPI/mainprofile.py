from fastapi import FastAPI, HTTPException, status
from schema import Profile
from database import Base,engine, SessionLocal
import model

Base.metadata.create_all(engine)
db = SessionLocal()

app = FastAPI()

#ProfileAPI

@app.get("/profiles",response_model=list[Profile])   #To view all data from database to user
def get_all_profile():
    profile = db.query(model.Profile).all()

    return profile

@app.get("/proflie/{profile_id}")       #To view a single record from database to user
def get_by_id(profile_id:int):
    # filter is used for conditions
    profile = db.query(model.profile).filter(model.Profile.profileID==profile_id).first()
    if profile is None:       #if given profile_id is not exist it will raise error else return profile.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")

    return profile

@app.post("/profile",                               # it will take data from user and store in database
          status_code=status.HTTP_201_CREATED)      # HTTP_201_CREATED to show that new recorded is stored
def create_order(profile:Profile):                  # here we are accepting the complete data
    new_profile = model.Profile(
        profileName=profile.profileName,
        productPrice=profile.profilePictureURL
    )
    db.add(new_profile)                             # add the data into table.
    db.commit()                                     #commit() is used to commit the current transaction
    return new_profile

#delete a single order using order_id
@app.delete('/profile/{profile_id}')
def delete_item(profile_id:int):
    profile_to_delete=db.query(model.Profile).filter(model.Profile.profileID==profile_id).first()

    if profile_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(profile_to_delete)
    db.commit()

    return profile_to_delete