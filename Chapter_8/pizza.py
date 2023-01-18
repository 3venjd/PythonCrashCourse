#def make_pizza(*toppings):
"""Print the list of toppings that have been requested"""
#    print(toppings)

#make_pizza('peperoni')
#make_pizza('mushrooms','green peppers','extra cheese')

#Version 2
"""summarize the pizza we are about to make"""
#def make_pizza(*toppings):
#    print("\nMaking a pizza with the following toppings:")
#    for topping in toppings:
#        print(f"- {topping}")


#make_pizza('peperoni')
#make_pizza('mushrooms','green peppers','extra cheese')

#Version 3
""" summarize the pizza we are about to make"""
#arbitrary argument always goes in the end
def make_pizza(size,*toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


#make_pizza(16,'peperoni')
#make_pizza(12,'mushrooms','green peppers','extra cheese')