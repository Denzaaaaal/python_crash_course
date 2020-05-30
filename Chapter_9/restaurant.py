class Restaurant:
    """Storing different types of restaurants"""

    def __init__(self, restaurant_name, cusine_type):
        """Creating attributes of the restaurant"""
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type

    def describe_restaurant(self):
        """Describing the restaurant"""
        print (f"The name of this restaurant is called {self.restaurant_name}.")
        print (f"This restaurant specialises in {self.cusine_type} cuisine.")

    def open_restaurant(self):
        """Telling the status of the restaurant"""
        print (f"{self.restaurant_name} is now Open!")

havet = Restaurant('havet', 'turkish')

havet.describe_restaurant()
havet.open_restaurant()