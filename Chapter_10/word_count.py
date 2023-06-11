def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename,encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        ##if you want to show a message use this way
        ##print(f"Sorry, the file {filename}, does not exist")
        
        ## else if you want to failing silently use pass
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"the file {filename} has about {num_words} words.")

##filename = 'text_files/alice.txt'
##count_words(filename)


filenames = ['text_files/alice.txt','siddhartha.txt', 'text_files/moby_dick.txt','text_files/little_women.txt']

for filename in filenames:
    count_words(filename)