#def greet_user():
#    """Display a simple greeting"""
#    print("Hello!")

#def greet_user(name):
#    """Display a simple greeting"""
#    print(f"Hello {name}")

#greet_user('Jesse')

#def get_formatted_name(first_name, last_name):
#    """Return a full name, neatly formatted"""
#    full_name = f"{first_name} {last_name}"
#    return full_name.title()

# this is an infinite loop!
#while True:
#    print("\nPlease tell me your name")
#    print("(enter 'q' at any tume to quit)")

#    f_name = input("First name: ")
#    if f_name == 'q':
#        break

#    l_name = input("Last name: ")
#    if l_name == 'q':
#        break

#    formatted_name = get_formatted_name(f_name,l_name)
#    print(f"\nHello, {formatted_name}")

def greet_users(names):
    """Print a simpple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
    

userNames = ['hannah', 'ty', 'margot']
greet_users(userNames)