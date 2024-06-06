from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    location: str
    receive_notifications: bool
    unit_preference: str

    def create_user(username, password, location, temp_receive_notifications, check = bool):
        """
        This method will be responsible for creating the user
        
        Args:
            username (str): The username
            password (str): The respective password for the username
            location (str): The user's location
            temp_receive_notifications (str): Temporary variable for receive_notifications
            receive_notifications (str): Confirmation for receiving notifications for the respective user
        """
        username = str(input("Enter the username: "))
        password = str(input("Enter your password: "))
        location = str(input("Select your location: "))
        while not check:
            temp_receive_notifications = str(input("Do you want to receive notifications? (1:yes, 2:no)"))
            if temp_receive_notifications == "1":
                receive_notifications = True
                check = True
            elif temp_receive_notifications == "2":
                receive_notifications = False
                check = True
            else:
                print("Error selecting, please choose again (1:yes, 2:no)")
                check = False

    def login(username, password):
        """
        This method will be used for logging into the application

        Args:
            username (str): The username
            password (str): The respective password for the username
        """

    def logout(self):
        pass

    def send_location(location = str):
        location = str(input("Select your location: "))
        return location

    def save_location(location = str):
        pass
