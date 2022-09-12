ordinal_numbers = [1,2,3,4,5,6,7,8,9]

for x in ordinal_numbers:
	if x == 1:
		print(f'{x}st')
	elif x == 2:
		print(f'{x}nd')
	elif x == 3:
		print(f'{x}rd')
	else:
		print(f'{x}th')