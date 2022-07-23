from typing import List, Text
from pydantic import BaseModel
from sqlalchemy import VARCHAR
from sqlalchemy import TEXT


class UserInfoBase(BaseModel):
    name=VARCHAR
    address=VARCHAR
    email=VARCHAR
    message=TEXT
    class Config:
        orm_mode = True

# class shreya_portfolio(UserInfoBase):
#     id: int
    
