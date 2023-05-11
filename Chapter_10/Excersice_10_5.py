file = 'text_files/programmingReasons.txt'

reasons = input('Why do you love programming?')
count = 0

while (reasons != 'Exit_salida'):
    count = count + 1
    with open(file,'a') as FileOpen:
        FileOpen.write(f'reason {count}) {reasons}.\n')
    
    reasons = input('another thing that you love programming?')