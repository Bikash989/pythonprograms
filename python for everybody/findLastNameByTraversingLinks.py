from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse

import ssl
import re

try:

    #ignore SSL certification errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = 'http://py4e-data.dr-chuck.net/known_by_Kahlan.html'

    html = urllib.request.urlopen(url, context=ctx).read()
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')


    for i in range(7):
        url = tags[17]
        res = url
        # print(url)
        x = re.findall('href="(.*)"', url.decode())
        url = str(x[0])    #re.findall returns list
        # print(type(url))
        # tags.clear()
        html = urllib.request.urlopen(url, context=ctx).read()
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        # if(i==6):
        #     print(url)
    extractName = re.findall('\">(.*)<', res.decode())
    # print("res: " + res.decode())
    print(extractName[0])



except Exception as e:
    print(e)
