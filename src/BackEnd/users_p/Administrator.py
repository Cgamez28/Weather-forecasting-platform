from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Administrator(BaseModel):
    name: str
    password: str


class AdministratorDB(Base):
    __tablename__ = 'administrators'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)