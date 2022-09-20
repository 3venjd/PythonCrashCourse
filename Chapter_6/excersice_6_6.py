favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'pil' : 'python'
}

users_poll = ['ana', 'sarah', 'federic', 'jen' , 'pil', 'rebeca']


for name in favorite_languages.keys():
	if name in users_poll:
		print(f"{name} you already taken the poll\n")
	elif name not in users_poll:
		print(f"{name} please take the poll\n")