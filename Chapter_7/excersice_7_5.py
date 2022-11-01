active = True

while active:
    age = int(input("How old are you? "))

    if age < 3:
        print("your ticket is free")
    elif age >= 3 and age <= 12:
        print("Your ticket cost $10")
    else:
        print("Your ticket cost $15")

    out = input("Do you want to continue? yes/not ")
    if out == "not":
        active = False