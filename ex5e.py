class InvalidLoginError(Exception):
    pass

class AccountLockedError(Exception):
    pass

class LoginSystem:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.attempts = 0
        self.max_attempts = 3

    # method to get username and password
    def login(self):
        try:
            # check if account is locked
            if self.attempts >= self.max_attempts:
                raise AccountLockedError("Account is locked due to too many failed attempts")

            # get user input
            user = input("Enter Username: ")
            pwd = input("Enter Password: ")

            # check credentials
            if user != self.username or pwd != self.password:
                self.attempts += 1
                raise InvalidLoginError("Invalid Username or Password")

            print("Login Successful")
            self.attempts = 0   # reset attempts after success

        except InvalidLoginError as e:
            print(e)

        except AccountLockedError as e:
            print(e)


# create object and call function
obj = LoginSystem("admin", "1234")

for i in range(5):   # allow multiple tries
    obj.login()