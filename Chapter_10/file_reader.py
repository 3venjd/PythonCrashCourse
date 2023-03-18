file_path = 'text_files/pi_digits.txt' #relative path
#file_path = 'D:\\Projects\\PythonCrashCourse\\Chapter_10\\text_files\\pi_digits.txt' # absolute path

with open(file_path) as file_object:
    lines = file_object.readlines() # readlines store each line in a value of list
    #print(lines[0])
    
    
    for line in lines:
        print(line.strip())
        
    
    
    #for line in file_object: # is to read line by line inside the document
    #    print(line.rstrip())
    #contents = file_object.read() #read all document

#print(contents.rstrip()) #rstrip remove the last blank line