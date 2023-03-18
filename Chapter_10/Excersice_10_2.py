path = 'text_files\\learnpython.txt'

with open(path) as txtFile:
    text = txtFile.readlines()

n = 0
for line in text:
    print(line.replace('-',str(n)).rstrip())
    n +=1