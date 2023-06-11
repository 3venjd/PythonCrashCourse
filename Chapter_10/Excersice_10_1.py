path = 'text_files\\learnPython.txt'

with open(path) as txtFile:
    text = txtFile.readlines()
    
for line in text:
    print(line.rstrip())