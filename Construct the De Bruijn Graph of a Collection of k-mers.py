import fileinput
def output(out):
    for i in range (len(out)):
        print(out[i][0] + ' -> ' + str(sorted(out[i][1])).replace("'","").replace("[","").replace("]","").replace(" ",""))
       

lines = [line.strip() for line in fileinput.input('rosalind_ba3e.txt')]
a = list()
check = 0;
for i in lines:
    k = [i[:-1],[i[1:]]]
    for j in range (len(a)):
        if(a[j][0]== k[0]):
            a[j][1].append(i[1:])
            check = 1
            break
    if(check == 0):
        a.append(k)
    check = 0
     
            
a.sort()
output(a)

