#from car import Car, ElectricCar
#import car
from car import Car
from electric_car import ElectricCar as EC

#my_new_car = Car('audi', 'a4', '2019')
#print(my_new_car.get_descriptive_name())

# change value directly
#my_new_car.odometer_reading = 23

# use a method to change value
#my_new_car.update_odometer(1)
#my_new_car.read_odometer()

#my_new_car.update_odometer(10)
#my_new_car.read_odometer()

#my_new_car.update_odometer(24)
#my_new_car.read_odometer()

#my_new_car.update_odometer(100)
#my_new_car.read_odometer()

## ---importing specific modules --- 
#my_beetle = Car('Volkswagen', 'beetle', 2019)
#print(my_beetle.get_descriptive_name())

#my_tesla = ElectricCar('Tesla', 'roadster', 2019)
#print(my_tesla.get_descriptive_name())

## ---importing all file --- 
#my_beetle = car.Car('Volksvagen', 'beetle', 2019)
#print(my_beetle.get_descriptive_name())

#my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
#print(my_tesla.get_descriptive_name())

## ---importing using alias --- 
my_beetle = Car('Volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = EC('Tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())