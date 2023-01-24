class Car:
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
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
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, miles):
        """Set the odometer reading to the given value
           Reject the change if it attempts to roll the odometer back
        """
        #if mileage >= self.odometer_reading:
        #    self.odometer_reading = mileage
        #else:
        #    print("You can't roll back an odometer")

        #Add the given amount to the odometer reading
        self.odometer_reading += miles
        

my_new_car = Car('audi','a4', '2019')
print(my_new_car.get_descriptive_name())

#change value directly
#my_new_car.odometer_reading = 23

#use a method to change value
my_new_car.update_odometer(1)
my_new_car.read_odometer()

my_new_car.update_odometer(10)
my_new_car.read_odometer()

my_new_car.update_odometer(24)
my_new_car.read_odometer()

my_new_car.update_odometer(100)
my_new_car.read_odometer()

