cities = {
	'medellin' : {
		'country' : 'colombia',
		'population' : 23401231,
		'fact' : 'the best place in the world'
	},
	'tokyo' : {
		'country' : 'japan',
		'population' : 28654786,
		'fact' : 'nice history'
	},
	'delhi' : {
		'country' : 'india',
		'population' : 41231321,
		'fact' : 'beautiful scenary'
	},
	'sao paulo' : {
		'country' : 'brazil',
		'population' : 51234213,
		'fact' : 'good dancers'
	},
}

for city, city_detail in cities.items():
	print(f"the city {city} is in the country {city_detail['country']}, it population is {city_detail['population']} and is a fact that {city_detail['fact']}")