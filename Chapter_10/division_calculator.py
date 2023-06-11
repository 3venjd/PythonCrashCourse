"""
try:
    print(5/0)
except ZeroDivisionError:
    print('You can´t divide by zero')
"""

print("Give me two numbers, and i'll divide them.")
print("enter 'q' to quit")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("Second Number: ")
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0")
    except ValueError:
        print("Please use numbers to divide")
    else:
        print (answer)