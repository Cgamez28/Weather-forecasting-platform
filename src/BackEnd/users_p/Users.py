from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict

router = APIRouter()

class User(BaseModel):
    username: str
    password: str
    location: str
    receive_notifications: bool
    unit_preference: Optional[str] = None
    
users_db: Dict[str, User] = {}

@router.post("/create_user")
def create_user(user: User):
    """
    This method will be responsible for creating the user
    
    Args:
        username (str): The username
        password (str): The respective password for the username
        location (str): The user's location
        temp_receive_notifications (str): Temporary variable for receive_notifications
        receive_notifications (str): Confirmation for receiving notifications for the respective user
    """
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    users_db[user.username] = user
    return {"message": "User created successfully"}

@router.post("/login")
def login(username:str, password: str):
    """
    This method will be used for logging into the application
    
    Args:
        username (str): The username
        password (str): The respective password for the username
    """
    user = users_db.get(username)
    if not user or user.password != password:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return{"message": f"Welcome{username}"}

@router.post("/logout")
def logout(username: str):
    """
    This method will be used for logout the account to the application
    
    Args:
        username (str): The username
    """
    user = users_db.get(username)
    if not user:
         raise HTTPException(status_code=400, detail="User not found")
    return{"message": f"Your account have been log out"}

@router.post("/send_location")
def send_location(username: str, location: str):
    """
    This method will be used for send the location to 
    
    Args:
        username (str): The username
        location (str): The respective location for the user
    """
    user = users_db(username)
    if not user:
         raise HTTPException(status_code=400, detail="User not found")
    user.location = location
    return{"message" : f"Location update for {username}", "location": location}

@router.post("/save_location")
def save_location(username: str, location: str):
    """
    This method will be used for send the location to 
    
    Args:
        username (str): The username
        location (str): The respective location for the user
    """
    user = users_db.get(username)
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    user.location = location
    return {"message": f"Location for {username} saved successfully", "location": location}
    







