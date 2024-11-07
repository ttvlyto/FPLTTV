
f = open("playerStats.txt", 'r')
strlen = len("overview__info")
players = open("links.txt")

print(strlen)
x = 0

for line in f:
    newstr = line
    x += 1
    i = 0
    if x==2830:
        print("something")
    if newstr == '******end, new player******\n':
        print('new player has been found, reset')
    while i < len(newstr):
        if newstr.__contains__('overview__info'):
            newstr = next(f)
            print(newstr.replace(" ", ""))


        else:
            i += 1

