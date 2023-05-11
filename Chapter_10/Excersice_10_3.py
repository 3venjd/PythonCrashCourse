filename = 'text_files/guest.txt'
userName = input('Please write your name')

with open(filename, 'w') as file_object:
    file_object.write(userName + ' ')