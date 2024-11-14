f = open('players.txt', 'r')
arr = []
for line in f:
    link = line[57:-500]

    x = 0

    for i in range(len(link)):
        if link[i] == '>':
            x = i
            arr.append(str(link[0:x-1]))
    
    print(link[0:x-1])
    print('\n')

f.close

l = open('links.txt', 'w' )
for x in arr:
    l.write(x + '\n')
