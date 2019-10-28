import fileinput
def MapLastToFirst(bwt):
    firstcol = sorted(bwt)
    map_index = []
    for char in bwt:
        index = firstcol.index(char)
        map_index.append(index)
        firstcol[index] = "*"
    return map_index
def bwmatching(FirstColumn,LastColumn,Pattern,LastToFirst):
    top = 0
    bottom = len(LastColumn) - 1
    while(top<=bottom):
        if(Pattern != ''):
            symbol = Pattern[-1]
            Pattern = Pattern[:-1]
            last_short = LastColumn[top : (bottom + 1)]
            if(symbol in last_short):
                topIndex = last_short.index(symbol) + top
                lastIndex = len(last_short) - last_short[::-1].index(symbol) + top - 1
                top    = LastToFirst[topIndex]
                bottom = LastToFirst[lastIndex]
            else:
                return 0
        else:
            return bottom - top + 1
        
lines = [line.strip() for line in fileinput.input('rosalind_ba9m.txt')]
LastColumn = lines[0]
FirstColumn = sorted(LastColumn)
LastToFirst = MapLastToFirst(LastColumn)
AllPattern = lines[1].split(" ")
Ans = ''
for pattern in AllPattern:
    Ans = Ans + str(bwmatching(FirstColumn,LastColumn,pattern,LastToFirst)) + ' '
print(Ans.strip())
