from car import Car

"""A set of classes used to represent gas and electric cars"""

class Battery:
    """A simple attempt to model a battery for an electric car"""
    
    def __init__(self, battery_size = 75):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}- kwh battery")
        
    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge")
    
    def upgrade_battery(self):
       if self.battery_size == 75:
           self.battery_size = 100
           print(f'Battery was upgraded to {self.battery_size}')
       else:
           print(f'Battery size is already')     
        
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class
           Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        #self.battery_size = 75
        self.battery = Battery()
        
    #def describe_battery(self):
    #    """Print a statement describing the battery size"""
    #    print(f"this car has a {self.battery_size} kwh battery")
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks"""
        print("This car doesn't need a gas tank!")