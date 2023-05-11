def count_words(file):
    
    try:
        with open(file,encoding='utf-8')as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"the file {file} has about {num_words} words.")

files = ["text_files/Cats.txt","text_files/Dogs2.txt"]

for file in files:
    count_words(file)