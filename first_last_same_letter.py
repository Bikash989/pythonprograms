# it checks if first and last letter of the word in a string is same or not
sentence = "The quick brown fox jumps overo a the lazy dog"

words = sentence.split(' ')
count = 0
for word in words:
    first = word[0]
    last = word[-1]
    if first == last:
        count += 1
print(count)
