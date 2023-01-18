short_quotes = ['hello list', 'im enjoy develop', 'sometimes is annoyong', 'but i love it', 'good bye']
send_messages = []

def show_messages(list):
    
    while list:
        quote = list.pop()
        print(f"{quote}")
        send_messages.append(quote) 


show_messages(short_quotes[:])
print("-----")
#for message in send_messages:
print(short_quotes)
print(f"{send_messages}")