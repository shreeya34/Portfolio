from typing import List
from sqlalchemy.orm import Session
from model import Portfolio
from database import Base,SessionLocal, engine
from turtle import st
from typing import Union
from pydantic import BaseModel
from schema import UserInfoBase


from fastapi import Depends, FastAPI, Form
app = FastAPI()

class ContactForm(BaseModel):
    name: str
    email: str
    message: Union[str, None] = None
    address: str

def get_db():
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        print(f"error {e}")
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test")
def read_test():
    return {"sucess":True,"message":"It works!" }

@app.post("/contact", response_model=UserInfoBase)
async def contact(cf: ContactForm, db: Session = Depends(get_db)):
    print(f"Name:{cf.name}")
    if not cf.name and cf.email:
        return {"message": "something went wrong!"}
    datastore = { "name": cf.name,
            "email": cf.email,
            "address": cf.address,
            "message" : cf.message}
    

    db_place = Portfolio(**datastore)
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place
   




