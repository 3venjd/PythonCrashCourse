requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print('Hold the anchovies')



available_topping = ['mushrooms','olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
list_requested_topping = ['mushrooms', 'french fries', 'extra cheese']

#print('mushrooms' in list_requested_topping)
#print('peperonni' in list_requested_topping)

for requested_topping in list_requested_topping:

	if requested_topping in available_topping:
		print(f"Adding {requested_topping}")
	else:
		print(f"Sorry, we don't have {requested_topping}")

print("\nFinished making yor pizza!")