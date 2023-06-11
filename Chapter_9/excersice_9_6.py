from excersice_9_1 import restaurant

class IceCreamStand(restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ['chocolate', 'vainila', 'red fruits', 'mandarine']
    
    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)

IceCream = IceCreamStand('pascasia','ice cream')
IceCream.show_flavors()