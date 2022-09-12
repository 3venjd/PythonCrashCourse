current_users = ['admin','regulator','3venjd','ti4g0','apolonseptimo']
new_users = ['Ti4g0','apolonseptimo','crawe','christos','fuuuuuuu','chiflamica']

for user in new_users:
	if user.lower() in current_users:
		print(f'the user {user} already exist, please choose another one')
	else:
		print(f'the user {user} is available')