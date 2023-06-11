from excersice_9_5 import User

class Admin(User):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

userAdmin = Admin('Evelio','Jimenez')
userAdmin.show_privileges()