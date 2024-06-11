from fastapi import APIRouter,  HTTPException
from DBconnection import PostgresConnection
from users_p import User
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

router_users = APIRouter()

load_dotenv()

engine = create_engine(
    f"postgresql://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASSWORD")}@{os.environ.get("DB_URL")}:{os.environ.get("DB_PORT")}/{os.environ.get("DB_NAME")}"
)
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String),
    Column("password", String),
    Column("location", String),
    Column("receive_notifications", String, default='False'),
    Column("preference_unit_measurement", String, default='metric')
    
)
metadata.create_all(engine)



@router_users.post("/create_user")
def create_user(user: User):
    """
    This method will be responsible for creating the user
    
    Args:
        username (str): The username
        password (str): The respective password for the username
        location (str): The user's location
        receive_notifications (str): Temporary variable for receive_notifications
        unit_preference (str): the unit of measurement of temperature
    """
    query = users.insert().values(username=user.username, password=user.password, location=user.location, receive_notifications=user.receive_notifications, preference_unit_measurement=user.preference_unit_measurement)
    session.execute(query)
    session.commit()
    return {"message": "User created successfully"}

@router_users.post("/login")
def login(username: str, password: str):
    """
    This method will be used for logging into the application
    
    Args:
        username (str): The username
        password (str): The respective password for the username
    """
    user = session.query(users).filter(users.c.username == username).first()
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.password != password:
        raise HTTPException(status_code=401, detail="Incorrect password")
    else:
        return True


@router_users.put("/update_location")
def update_location(username: str, location: str):
    """
    This method will be used for updating the user's location
    
    Args:
        username (str): The username
        location (str): The respective location for the user
    """
    user = session.query(users).filter(users.c.username == username).first()
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    update_query = users.update().where(users.c.username == username).values(location=location)
    session.execute(update_query)
    session.commit()
    
    return {"message": "Location updated successfully"}
