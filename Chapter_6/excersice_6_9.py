favorite_places = {
	'cristina': {
			'belmira',
			'mucura',
			'santa marta'
	},
	'evelio' : {
		'barichara',
		'san andres',
		'guatape'
	},
	'tiago' : {
		'carmen',
		'santa cruz',
		'del viento'
	},
	'jr' : {
		'miami',
		'new york',
		'atlanta'
	}
}

for name,place in favorite_places.items():
	print(f'{name} loves visit:')
	for pla in place:
		print(f'{pla}')
	print('\n')