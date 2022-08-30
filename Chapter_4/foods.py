my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print('my favorite foods are: ')
print(my_foods)
my_foods.append('cannoli')
print(my_foods)


print("\nMy friend's favorite foods are:")
friend_foods.append('ice cream')
print(friend_foods)

friend_foods = my_foods
print(friend_foods)