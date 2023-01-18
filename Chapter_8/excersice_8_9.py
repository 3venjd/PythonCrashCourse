short_quotes = ['hello list', 'im enjoy develop', 'sometimes is annoyong', 'but i love it', 'good bye']

def show_messages(list):
    while list:
        print(f"{list.pop()}")

show_messages(short_quotes)