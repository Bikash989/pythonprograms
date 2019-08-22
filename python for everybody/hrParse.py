from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import re
import sys
try:
    html = open('hackerank_data.html')
    # html = sys.stdin.read()     #for online submission
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a',class_='question-hyperlink')
    spans = soup('span',class_='relativetime')
    for tag,span in zip(tags,spans):
        val = str(tag)    
        # https://stackoverflow.com/questions/4666973/how-to-extract-the-substring-between-two-markers
        y = re.findall('/questions/(.*?)/',val)
        m = re.findall('>(.+?)<',val)
        p = re.findall('>(.+?)<',str(span))
        print(y[0]+";"+m[0]+";"+p[0])      

except Exception as e:
    print(e)
