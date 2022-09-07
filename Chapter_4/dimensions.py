dimensions = (200,50)
#print(dimensions[0])
#print(dimensions[1])

#Error because a tuple is inmutable
#dimensions[0] = 250

print('original dimensions')
for dim in dimensions:
	print(dim)

#to modify a tuple we need to change all data
dimensions = (400,100)

print('\nModified dimensions')
for dim in dimensions:
	print(dim)
