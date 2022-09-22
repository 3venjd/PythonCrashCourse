pet1 = {
	'kind' : 'dog',
	'owner' : 'evelio'
}

pet2 = {
	'kind' : 'cat',
	'owner' : 'cristina'
}

pet3 = {
	'kind' : 'horse',
	'owner' : 'rodrigo'
}

pet4 = {
	'kind' : 'fish',
	'owner' : 'katherine'
}

pet5 = {
	'kind' : 'mouse',
	'owner' : 'jr'
}


pets = {
	'oddy' : pet1,
	'magenta' : pet2,
	'pegasus' : pet3,
	'golden' : pet4,
	'bigotes' : pet5
}

for petname,pet_detail in pets.items():
	print(f"{petname} is a {pet_detail['kind']} "
		f"and it owner is {pet_detail['owner']}")