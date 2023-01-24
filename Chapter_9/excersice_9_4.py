class restaurant:
    def __init__(self,name,cuisine_type):
        """Init method"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Little description of the restaurant"""
        print(f"the restaurant {self.name} has a cuisine type like {self.cuisine_type}")

    def open_restaurant(self):
        print(f"the restuaurant {self.name} is open")

    def set_number_serverd(self):
        print(f"the number served is {self.number_served}")

    def increment_number_served(self,num):
        self.number_served += num



restaurant1 = restaurant('los cholos', 'soup')
restaurant1.set_number_serverd()
restaurant1.increment_number_served(3)
restaurant1.set_number_serverd()
restaurant1.increment_number_served(1)
restaurant1.set_number_serverd()
restaurant1.increment_number_served(6)
restaurant1.set_number_serverd()