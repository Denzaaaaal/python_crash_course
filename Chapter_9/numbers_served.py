class Restaurant:
    """Storing different types of restaurants"""

    def __init__(self, restaurant_name, cusine_type):
        """Creating attributes of the restaurant"""
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describing the restaurant"""
        print (f"\nThe name of this restaurant is called {self.restaurant_name}.")
        print (f"This restaurant specialises in {self.cusine_type} cuisine.")
        print (f"The number of customers being served in this restaurant is {self.number_served}")

    def open_restaurant(self):
        """Telling the status of the restaurant"""
        print (f"{self.restaurant_name} is now Open!")

    def set_number_served(self, customers):
        """Attribute explaining the number of customers served"""
        self.number_served = customers

    def increment_number_served(self, increment_number):
        """Adding increment to customers being served"""
        self.number_served += increment_number

havet = Restaurant('havet', 'turkish')

havet.describe_restaurant()
havet.open_restaurant()
havet.set_number_served(28)

havet.describe_restaurant()
havet.increment_number_served(13)
havet.describe_restaurant()
