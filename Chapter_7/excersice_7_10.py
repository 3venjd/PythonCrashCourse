places = {}

polling_active = True

while polling_activate:
    #prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("if you could visit one place in the worl, where would you go? ")

    #store the response in the dictionary
    places[name] = response

    #Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no)")
    
    if repeat == "no":
        polling_activate = False
    
#polling is complete. Show the results
print("\n--- Poll Results ---")

for name, response in places.items():
    print(f"{name} would like to climb {response}.")