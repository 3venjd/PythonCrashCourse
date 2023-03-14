class User:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.logging_attempts = 0

    def describe_user(self):
        """Little description of the user"""
        print(f"the user {self.firstName} {self.lastName} has arrives")

    def greet_user(self):
        print(f"hello {self.firstName} {self.lastName}, welcome")

    def increment_login_attempts(self):
        self.logging_attempts += 1
    
    def reset_login_attempts(self):
        self.logging_attempts = 0

