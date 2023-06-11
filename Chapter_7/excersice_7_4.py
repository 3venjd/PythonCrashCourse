from operator import truediv
from pickle import TRUE


active = TRUE

while active:
    topping = input("insert a topping to add ")
    if topping == "quit":
        active = False
    else:
        print(f"you added {topping} to the pizza")
