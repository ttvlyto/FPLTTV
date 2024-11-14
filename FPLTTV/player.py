##opens saved HTML written to players.txt
##parses iterate through string to find important data, like player links, name and pos



player = open("players.txt", "r")
PlayerList = []
i = 0
for line in player:

    PlayerList.append(line.strip())
    i = i + 1

string = PlayerList[0]
index = 0

i = 0
start = 0
end = 0

link = []
name = []
pos = []
while index < 100:
    if string[i:i+4] == "href":
        start = i
        while string[i] != ">":
            i = i + 1
        end = i
        print(string[start:end])

        link.append(string[start:end])

    if string[i:i+8] == "position":
        start = i
        while string[i] != "<":
            i = i + 1
        end = i
        print(string[start:end] + "\n")
        pos.append(string[start:end])
        name = link[index]
        name = name[38:-9]
        i = 0
        while name[i] != "/":
            i = i + 1
        name = name[i+1:-1]
        name = name.replace("-", " ")

        print(name)

        index += 1

        i = 0
        string = PlayerList[index]

    else:
        i = i + 1



##print(listy)
f = open("links.txt", "w")
for x in range(0,100):
    string = link[x]
    f.write(string[8:-1] + "\n")
f.close()

