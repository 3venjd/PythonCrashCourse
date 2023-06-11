FileText = 'text_files/guest_book.txt'

UserName = input('Please write your name ')

while(UserName != 'exit_final'):
    print(f'hi {UserName} welcome to the system')
    
    with open(FileText, 'a') as File_Object:
        File_Object.write(f'the user {UserName} login in the system.\n')
    
    UserName = input('Please write your name ')