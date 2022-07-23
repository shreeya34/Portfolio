from cgitb import text
from sqlalchemy import VARCHAR
from sqlalchemy.schema import Column
from sqlalchemy.types import VARCHAR, Integer, Text
from database import Base
class Portfolio(Base):
    __tablename__ = "shreya_portfolio"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(100))
    address = Column((VARCHAR(100)))
    email= Column(VARCHAR(100))
    message = Column(Text(1000))
    