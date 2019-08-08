def FindSubString (s, x):
    idx = 0
    l=[]
    flag = 0
    if(len(x) < len(s)):
        for c in x:
            val = s.find(c)
            if(val!=-1 and val not in l):
                l.append(val)
            else:
                flag = 1
                break
    elif(len(x) == len(s) and x == s):
        return s
    else:
        flag = 1

    if(flag == 1):
        return -1
    else:
        return s[min(l):max(l)+1]


T = int(input())
for _ in range(T):
    A = input()
    B = input()

    out_ = FindSubString(A, B)
    print (out_)
