class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """initalize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print (f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set an odometer reading to the given value.
        Reject the change if it attempts to roll back the odometer.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print ("You cannot roll back an odometer!")

    def increment_odometer(self, miles):
        """Adding the given amount to the odemeter reading"""
        self.odometer_reading += miles

class Battery:
    """A simple model for a battery in an electric car"""
    
    def __init__(self, battery_size=75):
        """initialise battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print (f"This car has a {self.battery_size}-KWh battery.")

    def get_range(self):
        """print a statement about the range the battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print (f"This car will go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        initialise attributes of the parent class.
        Then initalise attributes specific to an electri car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2009)
print (my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()