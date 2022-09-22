favoriteNumber = {
		'wendy' : {2, 5, 1},
		'cris' : {4, 3, 0},
		'eve' : {8, 7, 9 },
		'kat' : {12, 19 ,1}
		}
for name,num in favoriteNumber.items():
	print(f"the user {name} says the best numers are: ")
	print(f"{favoriteNumber[name]}")