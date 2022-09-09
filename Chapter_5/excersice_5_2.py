string_1 = 'test1'
string_2 = 'Test1'

if string_1 == string_2:
	print('Data equal')
else:
	print('is not Equal')


string_3 = string_2.lower()

if string_1 == string_3:
	print('is equal')
else:
	print('is not Equal')


num1 = 43
num2 = 12

if num1 == num2:
	print('the numbers are equal')
else:
	print('the numbers are not equal')

if num1 > num2:
	print('number 1 is greater than number 2')
else:
	print('number 1 is not greater than number 2')

if num1 < num2:
	print('number 2 is greater than number 1')
else:
	print('number 2 is not greater than number 1')

if num1 >= num2:
	print('number 1 is greater or Equal than number 2')
else:
	print('number 1 is not greater or Equal than number 2')

number_list = [5,2,8,4,0,1,6]
number1 = 5
number2 = 9

if number1 not in number_list:
	print(f'the number {number1} not in the list')
else:
	print(f'the number {number1} is in the list')

if number2 in number_list:
	print(f'the number {number2} is in the list')
else:
	print(f'the number {number2} not in the list')

