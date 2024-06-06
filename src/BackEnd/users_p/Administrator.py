class Admin:
    def __init__(self):
        self.name = "Admin"
        self.__password = "Adm1nP@ssw0rd"
        self.authenticated = False

    def login(self, name, password):
        entered_name = str(input("Enter the username: "))
        if entered_name == name:
            while not self.authenticated:
                entered_password = str(input("Enter your password: "))
                if entered_password == password:
                    self.authenticated = True
                    print("Successfully logged in")
                else:
                    print("Incorrect password, please try again")

    def logout(self):
        pass
  