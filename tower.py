def FindSubString (s, x):
    idx = 0
    l=[]
    flag = 0
    if(len(x) < len(s)):
        find_first = s.find(x[0], 0) # for 1st char
        if(find_first != -1):
            l.append(find_first)
            idx = 0
            x = x[1:]
            for c in x:
                val = s.find(c,l[idx])
                if(val != -1):   # check for c and start from idx
                    l.append(val)
                    if(l != sorted(l)):
                        flag = 1
                        break
                    idx += 1
                else:
                    flag = 1
                    break
        else:
            flag = 1
    elif(len(x) == len(s) and x == s):
        return s
    else:
        flag = 1

    if(flag == 1):
        return -1
    else:
        return s[l[0]:l[-1]+1]


T = int(input())
for _ in range(T):
    A = input()
    B = input()

    out_ = FindSubString(A, B)
    print (out_)
