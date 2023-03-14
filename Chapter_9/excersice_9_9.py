class Car:
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
        
    def update_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print(f"This car has a {self.battery_size} - kwh battery")
    
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge")
    
    def upgrade_battery(self):
        if self.battery_size == 75:
            self.battery_size == 100
            print(f'Battery was upgrade to {self.battery_size}')
        else:
            print(f'Battery size is already')
            
            
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super.__init__(make, model, year)
        self.battery = Battery()
        
    def fill_gass_tank(self):
        print("this car doesn't need a gas tank!")
    
my_tesla = ElectricCar('tesla', "model's", '2019')
my_tesla.battery.get_range()
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()