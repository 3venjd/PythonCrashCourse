from excersice_9_5 import User

class Admin(User):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName)
        self.privileges = Privileges()
    
    def show_privileges(self):
        for privilege in self.privileges.priv:
            print(privilege)
            
class Privileges:
    def __init__(self, priv  = ['can add post', 'can delete post', 'can ban user']):
        self.priv = priv
        
    

userAdmin = Admin('Evelio','Jimenez')
userAdmin.show_privileges()