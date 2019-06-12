# Use the file mbox-short.txt as the file name
# file location: https://www.py4e.com/code3/mbox-short.txt
fname = input("Enter file name: ")
fh = open(fname)
total = 0.0
n = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    s = float((line[line.find(':')+1:len(line)].strip()))
    total += s
    n += 1
    
avg = total/n 



print("Average spam confidence:",avg)
