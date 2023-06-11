from excersice_9_5 import User

user1 = User('Jr','Lopez')

print(f"the user 1 is {user1.firstName} {user1.lastName}")
user1.describe_user()
user1.greet_user()
for i in range(3):
    user1.increment_login_attempts()
    print(f"number of attempts {user1.logging_attempts}")

user1.reset_login_attempts()
print(f"number of attempts {user1.logging_attempts}")