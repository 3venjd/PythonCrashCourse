favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'pil' : 'python'
}

#language = favorite_languages['sarah'].title()

#print(f"Sarah's favorite language is {language}")

#for name, language in favorite_languages.items():
#	print(f"{name.title()}'s favorite languages is {language.title()}.")

#print only the keys
#for x in favorite_languages.keys():
#	print(x.title())

#	friends = ['pil', 'sarah']
#	if name in friends:
#		language = favorite_languages[name].title()
#		print(f"\t{name.title()}, i see you love {language}")

#if 'erin' not in favorite_languages.keys():
	#print("Erin, please take our poll")

#for name in sorted(favorite_languages.keys()):
#	print(f"{name.title()}, thank you for taking the poll")

print("the following languages have been mentionated: ")

for languages in favorite_languages.values():
	print(languages.title())
