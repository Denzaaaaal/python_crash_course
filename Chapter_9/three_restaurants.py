class Restaurant:
    """Storing different types of restaurants"""

    def __init__(self, restaurant_name, cusine_type):
        """Creating attributes of the restaurant"""
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type

    def describe_restaurant(self):
        """Describing the restaurant"""
        print (f"\nThe name of this restaurant is called {self.restaurant_name}.")
        print (f"This restaurant specialises in {self.cusine_type} cuisine.")

    def open_restaurant(self):
        """Telling the status of the restaurant"""
        print (f"{self.restaurant_name} is now Open!")

# Importing the restaurants
havet = Restaurant('havet', 'turkish')
subway = Restaurant('subway', 'sandwitch')
turtle_bay = Restaurant('tutle bay', 'jamaican')

# Printing the status of the restaurant
havet.describe_restaurant()
havet.open_restaurant()
subway.describe_restaurant()
subway.open_restaurant()
turtle_bay.describe_restaurant()
turtle_bay.open_restaurant()