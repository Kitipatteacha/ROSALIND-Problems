import fileinput
lines = [line.strip() for line in fileinput.input('Input.txt')]
String = ''
Transform = list()
ANS = ''
for i in lines:
    String = i
BWT = String
Transform = sorted(BWT)
for i in range(len(BWT)-1):
    for j in range(len(BWT)):
        Transform[j] = BWT[j] + Transform[j]
    Transform = sorted(Transform)
for i in Transform:
    if(i[-1]=='$'):
        print(i)

