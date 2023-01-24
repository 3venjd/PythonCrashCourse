class restaurant:
    def __init__(self,name,cuisine_type):
        """Init method"""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Little description of the restaurant"""
        print(f"the restaurant {self.name} has a cuisine type like {self.cuisine_type}")

    def open_restaurant(self):
        print(f"the restuaurant {self.name} is open")


restaurant1 = restaurant('los cholos', 'soup')
restaurant2 = restaurant('los perritos', 'hot dog')
restaurant3 = restaurant('quesudos', 'hamburguer')

print(f"the restaurant is called {restaurant1.name} and the main food is {restaurant1.cuisine_type}")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

print(f"the restaurant is called {restaurant2.name} and the main food is {restaurant2.cuisine_type}")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

print(f"the restaurant is called {restaurant3.name} and the main food is {restaurant3.cuisine_type}")
restaurant3.describe_restaurant()
restaurant3.open_restaurant()