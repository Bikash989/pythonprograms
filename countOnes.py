def countOnes(n):
    c = 0
    i = 0
    while i < 8:
        c += n & 1
        print(n&1, end = " ")  #gives the binary representation of n
        n >>= 1   # left shift by one


        i +=1

    print("\nTotal number of one's is ", c)

countOnes(20)
