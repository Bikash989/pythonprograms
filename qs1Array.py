'''
    qs1.Array
    Suppose we have an array a1,a2,...an,b1,b2,...,bn. Implement an
    algorithm to change this array to a1,b1,a2,b2,..,an,bn
'''
def solve(l):
    iter1 = iter(l)
    iter2 = iter(l[len(l)//2:])
    res = []
    for a,b in zip(iter1,iter2):
        res.append(a)
        res.append(b)
    return res

def inplace(l):
    idx = len(l)//2
    for i in range(1,len(l),2):
        l.insert(i,l.pop(idx))
        idx += 1
    return l

if __name__ == "__main__":
    input_string = input("Enter numbers seperated by space\n")
    list = input_string.split()
    myList = []
    for num in list:
        myList.append(int(num))
    print("Input  :: ",myList)
    l = myList
    myList = solve(myList)
    print("Output :: ",myList)
    print(inplace(l))
