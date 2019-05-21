# program that accepts a url address from the user and prints the links
# import networking library to open connections to the webpage and load file
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
# disable secure socket layer certification error, if any
import ssl


try:
    #ignore SSL certification errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    #url = input("Enter url: ")
    url = 'http://scipy-lectures.org/'
    if url == '':
        print("Enter an url next time")
    else:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        #retrieve anchor tags
        tags = soup('a')
        for tag in tags:
            line = tag.get('href', None)
            if(line != None and line.endswith('.pdf')):
                print(line)
except Exception as e:
    print(e)

# http://data.pr4e.org/romeo.txt testing site
