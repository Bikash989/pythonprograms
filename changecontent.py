f = open('cs229PdfLinks.txt','w')

with open('cs229_stanford_notes.txt', 'r') as fh:
    for line in fh:
        line = 'http://cs229.stanford.edu/notes/' + line
        f.write(line)
f.close()
