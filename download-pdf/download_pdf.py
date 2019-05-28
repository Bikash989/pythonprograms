import requests
#beware of relative path, the file contains relative path
# i.e why throwing error
# need to modify find-pdf-link-in-webpage.property
#will do it later
#for now assuming the file contains full path

fh = open('cs229PdfLinks.txt','r')
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

# url = 'http://www.hrecos.org//images/Data/forweb/HRTVBSH.Metadata.pdf'
# r = requests.get(url, stream=True)
# chunk_size = 2000
# with open('mypdf.pdf', 'wb') as fd:
#     for chunk in r.iter_content(chunk_size):
#         fd.write(chunk)
