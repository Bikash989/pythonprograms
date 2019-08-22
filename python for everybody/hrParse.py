from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse

import re

try:
    html = open('hackerank_data.html')
    # html = sys.stdin.read()     #for online submission
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a',class_='question-hyperlink')
    spans = soup('span',class_='relativetime')
    first = []
    second = []
    for tag in tags:
        val = str(tag).rstrip()       
        # https://stackoverflow.com/questions/4666973/how-to-extract-the-substring-between-two-markers
        y = re.findall('/questions/(.*?)/',val)
        m = re.findall('>(.+?)<',val)
        first.append(y[0]+";"+m[0])

    for span in spans:
        y = re.findall('>(.+?)<',str(span))
        second.append(y[0])

    #print the result
    for i in range(0,len(first)):
        print(first[i]+";"+second[i])
except Exception as e:
    print(e)
