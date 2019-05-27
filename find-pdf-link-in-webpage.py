# program that accepts a url address from the user and prints the links
# import networking library to open connections to the webpage and load file
import urllib.request, urllib.parse, urllib.error
#before using BeautifulSoup library, install: pip3 install BeautifulSoup
from bs4 import BeautifulSoup
# disable secure socket layer certification error, if any
import ssl
import re
import os #to delete the empty file, if no links found


try:
    #ignore SSL certification errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE


    url = input("Enter full url(eg: http://mit.edu): ")
    if url == '':
        print("Invalid Url")
    else:

        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        #retrieve anchor tags
        tags = soup('a')
        print("Connection established")
        filename = input('Enter file name to store the links (eg: mylinks.txt): ')
        fh = open(filename,'w')
        link = 0 #to indicate if copied any links
        for tag in tags:
            line = tag.get('href', None)

            if(line != None and line.endswith('.pdf')):
                # print(line)
                line = line + "\n"
                fh.write(line)
                link += 1

    fh.close() # release resource
    if link > 0:
        print(link , " links copied!")
        print("Check the file: ",filename)
    else:
        os.remove(filename)
        print('No links copied, file removed')

except Exception as e:
    print(e)
