DATABASE_URL = "mysql+mysqlconnector://root@localhost:4306/portfolio"
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "mysql+mysqlconnector://root@localhost:4306/portfolio"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()