from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse

import ssl
import re

try:
    #ignore SSL certification errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = 'http://py4e-data.dr-chuck.net/comments_232683.html'

    html = urllib.request.urlopen(url, context=ctx).read() #read whole page
    soup = BeautifulSoup(html, 'html.parser')
    number = list()
    #now we retrive span tags
    tags = soup('span')
    s = 0
    for tag in tags:

        # print(tag)
        # f = re.findall('^<span class="comments">(.*)<',tag)
        # print(f)
        x = re.findall('^<span class=\"comments\">([0-9]+)<', tag.decode())
        number.append(x)

    for val in number:
        s += int(val[0])
    print(s)
except Exception as e:
    print(e)
