import fileinput
lines = [line.strip() for line in fileinput.input('Input.txt')]
String = ''
BWT = list()
ANS = ''
for i in lines:
    String = i
for i in range (len(String)):
    String = String[1:] + String[0]
    BWT.append(String)
BWT = sorted(BWT)
for i in BWT:
    ANS = ANS + i[-1]
print(ANS)


