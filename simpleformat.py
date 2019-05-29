inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweetpant, 25, 100"]


i=0

while i < len(inventory):
    word = inventory[i]
    words = word.split(',')

    print("The store has {} {}, each for {} USD.".format(words[1].strip(), words[0].strip(), words[2].strip()))

    i += 1
