listUsers = ['admin','fallen','even','hector','raimi']
#listUsers = []
userName = 'r'

if userName in listUsers:
	print('Hello admin, would you like to see a status report')
elif len(listUsers) <= 0:
	print('We need to find some users')
else:
	print(f'Hello {userName}, thank you for logging in again')
	