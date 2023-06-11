class User:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def describe_user(self):
        """Little description of the user"""
        print(f"the user {self.firstName} {self.lastName} has arrives")

    def greet_user(self):
        print(f"hello {self.firstName} {self.lastName}, welcome")

user1 = User('Jr','Lopez')

print(f"the user 1 is {user1.firstName} {user1.lastName}")
user1.describe_user()
user1.greet_user()