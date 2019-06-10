import urllib.request, urllib.parse, urllib.error #for retrieving data from url
import xml.etree.ElementTree as ET  #for parsing xml data
import ssl

try:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input("Enter Location: ")
    # url = "http://py4e-data.dr-chuck.net/comments_232685.xml"
    print("Retrieving ",url)
    count = 0
    xml = urllib.request.urlopen(url, context = ctx).read()  #read xml from url
    print("Retrieved ",len(xml), "characters")
    tree = ET.fromstring(xml)  #create tree from xml
    lst = tree.findall('comments/comment') #don't include toplevel element
    print("Count: ", len(lst))
    sum = 0
    for item in lst:
        ct = item.find('count').text
        sum += int(ct)
    print("Sum: ",sum)
    #print('comment: ',tree.find('comment').text)

except Exception as e:
    print(e)
