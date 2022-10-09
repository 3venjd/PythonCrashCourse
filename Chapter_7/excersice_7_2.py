tables_number = input("how many people are in the restaurant? ")
tables_number = int(tables_number)

if tables_number > 8:
    print("your group need wait for a table")
else:
    print("a table is ready")