
while True:
    
    Number1 = input("Write the first number ")

    Number2 = input("Write the second number ")

    try:
        result = int(Number1) + int(Number2)
    except ValueError:
        break
    else:
        print(f"the result is {result} ")

