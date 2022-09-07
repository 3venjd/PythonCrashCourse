my_pizzas = ['margarita', 'hawaiana', 'sweet pork', 'sweet pork philadelpia']

friend_pizzas = my_pizzas[:]

my_pizzas.append('bacon supreme')

friend_pizzas.append('paisa')

print(f'my favorite pizzas are: ')

for pizza in my_pizzas:
	print(pizza)

print(f"my friend's favorite pizza are: ")
for pizza in friend_pizzas:
	print(pizza)