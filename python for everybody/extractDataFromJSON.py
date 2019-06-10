import urllib.request, urllib.parse, urllib.error
import json
import ssl
try:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input("Enter Location: ")

    print("Retrieving ",url)
    js = urllib.request.urlopen(url, context = ctx).read().decode()  #read json from url
    print("Retrieved ",len(js), "characters")

    info = json.loads(js) #returns lists conatining dictionary inside dictioanry ...
    # print(type(info))

    lstDict = info['comments'] #get the comments as list of dictionary
    # print(type(lstDict))
    print("Count: ",len(lstDict))
    totalCount = 0
    #now traverse the list and add the count
    for item in lstDict:
        val = item['count']
        totalCount += int(val)
    print("Sum: ",totalCount)
except Exception as e:
    print(e)



'''
eg:
    {
  "note":"This file contains the sample data for testing",
  "comments":[
    {
      "name":"Romina",
      "count":97
    },
    {
      "name":"Laurie",
      "count":97
    },
    {
      "name":"Bayli",
      "count":90
    },
    ...

'''
