import fileinput
lines = [line.strip() for line in fileinput.input('rosalind_tfsq.txt')]
count = 1
for line in lines:
    if(count == 1):
        check = 1
        print('>' + line[1:])
    if(count == 2):
         print(line)
    if(count == 4):
        count = 0
    count = count + 1

        
    
