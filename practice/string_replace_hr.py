def getdna(s):
    rev = s[::-1]
    res = ""
    for c in rev:
        if(c is 'A'):
            res += 'T'
        elif(c is 'C'):
            res += 'G'
        elif(c is 'G'):
            res += 'C'
        elif(c is 'T'):
            res += 'A'
    return res

def do():
    s = input()
    print(getdna(s))
do()