class Users:
    """Storing user information"""

    def __init__(self, first_name, last_name, age, location):
        """Setting up attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Describing user details"""
        print (f"\nFirst name: {self.first_name}")
        print (f"Last name: {self.last_name}")
        print (f"Age: {self.age}")
        print (f"Location: {self.location}")
        print (f"Login Attempts: {self.login_attempts}")

    def greet_user(self):
        """Printing greeting message"""
        print (f"\nHi {self.first_name} {self.last_name}, How are you doing today?")

    def increment_login_attempt(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

denzel = Users('denzel', 'douglas', 26, 'london')

denzel.describe_user()
denzel.increment_login_attempt()
denzel.increment_login_attempt()
denzel.describe_user()
denzel.reset_login_attempts()
denzel.describe_user()
denzel.greet_user()

