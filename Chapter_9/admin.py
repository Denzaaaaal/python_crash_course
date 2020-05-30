class Users:
    """Storing user information"""

    def __init__(self, first_name, last_name, age, location):
        """Setting up attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        """Describing user details"""
        print (f"\nFirst name: {self.first_name}")
        print (f"Last name: {self.last_name}")
        print (f"Age: {self.age}")
        print (f"Location: {self.location}")

    def greet_user(self):
        """Printing greeting message"""
        print (f"\nHi {self.first_name} {self.last_name}, How are you doing today?")

class Admin(Users):
    """Storing admin information"""

    def __init__(self, first_name, last_name, age, location, priviliges):
        """Making attributes for admin user"""
        super().__init__(first_name, last_name, age, location)
        self.priviliges = priviliges

    def describe_user(self):
        """Describing user details"""
        super().describe_user()

    def show_priviliges(self):
        print ("This users has additional priviliges that include: ")
        for privilige in self.priviliges:
            print (f"- {privilige}")

administrator = Admin('Administrator', 1, 26, 'london', ['can add post', 'can delete post', 'can ban user'])
administrator.describe_user()
administrator.show_priviliges()