try:
    fname = input("Enter file name: ")

    count = 0
    fh = open(fname)
    for line in fh:
        if not line.startswith('From:'):
            continue
        words = line.split()
        print(words[1])
        count += 1

    print("There were", count, "lines in the file with From as the first word")

except Exception as e:
    print('error')
