sandwich_order = ['tomatoe','tuna','meat','chicken','bacon']

finished_sandwiches = []

active_orders = True

while sandwich_order:
    finished_sandwich = sandwich_order.pop()
    print(f"i made your {finished_sandwich} sandwich")
    finished_sandwiches.append(finished_sandwich)

print(f"the next sandwich were made {finished_sandwiches}")
