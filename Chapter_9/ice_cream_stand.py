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

class IceCremStand(Restaurant):
    """Setting up new class for ice cream stands"""
    
    def __init__(self, restaurant_name, cusine_type, flavours):
        """Describing attributes of the ice cream bar"""
        super().__init__(restaurant_name, cusine_type)
        self.flavours = flavours

    def describe_restaurant(self):
        """Describing attributes of the ice cream stand"""
        super().describe_restaurant()
        print(f"The flavours we are sellngs are: ")
        for flavour in self.flavours:
            print (f"- {flavour}")


baskin = IceCremStand('baskin robbins', 'desert', ['chocolate', 'vanilla'])
baskin.describe_restaurant()