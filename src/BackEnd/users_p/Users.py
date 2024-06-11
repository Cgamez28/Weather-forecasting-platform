from pydantic import BaseModel


class User(BaseModel):
    id: int = None
    username: str
    password: str
    location: str
    receive_notifications: str
    preference_unit_measurement: str
    
    def create_user(username: str, password: str, location: str, receive_notifications: str, unit_preference: str):
        """
        This method will be responsible for creating the user

        Args:
            username (str): The username
            password (str): The respective password for the username
            location (str): The user's location
            receive_notifications (str): Temporary variable for receive_notifications
            unit_preference (str): the unit of measurement of temperature
        """
        pass

    def login(username: str, password: str):
        """
        This method will be used for logging into the application

        Args:
            username (str): The username
            password (str): The respective password for the username
        """
        pass

    def logout(self):
        pass

    def send_location(location = str):
        location = str(input("Select your location: "))
        return location
    
    
    class Config:
        orm_mode: True
 
                 

