print("Python")

#initial space (tab)
print("\tPython") 

#new line
print("Languages:\nPython\nC#\nJavascript")

#combine previuos
print("Languages:\n\tPython\n\tC#\n\tJavascript")

#delete the final space
favorite_language = 'Python '
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)

#delete initial space
favorite_language = ' Python'
print(favorite_language)
favorite_language = favorite_language.lstrip()
print(favorite_language)

#remove initial and end whitespaces
favorite_language = ' Python is nice'
print(favorite_language)
favorite_language = favorite_language.strip()
print(favorite_language)