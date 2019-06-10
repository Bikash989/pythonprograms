import requests

fname = input("Enter file name: ")
try:
    fh = open(fname,'r')
    for line in fh:
        link = line.strip()
        # print('link: ',link)
        r = requests.get(link, stream=True)
        chunk_size = 2000

        #file name
        words = link.split('/')
        fname = words[len(words)-1]
        print('Downloading file from ', link)
        with open(fname,'wb') as fd:
            for chunk in r.iter_content(chunk_size):
                fd.write(chunk)
        print("Done.")
    print('\nDownloaded')
    fh.close()
except Exception as e:
    print(e)
