#urllib makes socket communiation and HTTP communications a lot better
#underneath it's make a socket call, Get 'address',portno ...
import urllib.request, urllib.parse, urllib.error
fh = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count = dict()
for line in fh:
    words = line.decode().strip().split(' ')
    for word in words:
        count[word] = count.get(word,0) + 1
# print(count)
# print(max(count))
max_word = None
max_count = 0
for k,v in count.items():
    print(k,v)
    if max_word is None or max_count < v:
        max_word = k
        max_count = v

print(max_word)
print(max_count)
