def count_words(file,word):
    
    try:
        with open(file,encoding='utf-8')as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        totalcount = 0
        words = contents.split()
        countWord = words.count(word)
        print(f"in the file {file} the word {word} appears {countWord} times.\n")
    

files = ["text_files/Cats.txt","text_files/Dogs.txt",'text_files/alice.txt',
         'siddhartha.txt', 'text_files/moby_dick.txt','text_files/little_women.txt']

for file in files:
    count_words(file,'happy')