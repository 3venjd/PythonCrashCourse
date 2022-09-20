programming_words = {
	'int' : 'type of data that save int values',
	 'list' : 'array that contains data',
	 'tuple' : 'unmutable list',
	 'Dictionary' : 'list that contains data with key-value'
	  }

for words,meaning in programming_words.items():
	print(f"{words} is a {meaning}\n")

programming_words['float'] = 'value with decimal points'

programming_words['string'] = 'value that contains characters'


print('Added values')

for words,meaning in programming_words.items():
	print(f"{words} is a {meaning}\n")