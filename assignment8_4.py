fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()

    words = line.split()

    for word in words:
        if not word in lst:
            lst.append(word)

lst.sort() #sort inplace, so can't use like this print(lst.sort()) -> will return None
print(lst)
