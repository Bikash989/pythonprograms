import json
data = '''
[
    {
        "id": "001",
        "x": "2",
        "name": "Bikash"
    },
    {
        "id": "002",
        "x": "3",
        "name": "Rakesh"
    }
]'''
info = json.loads(data) #return lists containing dictionary
print('User count: ', len(info))

for item in info:
    print('Name: ',item['name'],end=" ") #item accessed as dictionary and iterated as list
    print('Id: ', item['id'])
