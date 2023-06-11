sandwich_order = ['tomatoe','pastrami','tuna','meat','pastrami','chicken','pastrami','bacon']

finished_sandwiches = []

active_orders = True

print(f"the deli has run out of pastrami")

while sandwich_order:
    
    finished_sandwich = sandwich_order.pop()
    if finished_sandwich != "pastrami":
        print(f"i made your {finished_sandwich} sandwich")
        finished_sandwiches.append(finished_sandwich)

print(f"the next sandwich were made {finished_sandwiches}")
