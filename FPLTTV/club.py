class Club:
    name = ""
    link = ""
    players = []
    def __init__(self, Name, link, Players = None):
        self.name = Name
        self.link = link
        self.players = Players



f = open("link.txt", 'r')
clubs = []
for line in f:
        # Print each line
    clubs.append(line.strip())
f.close()
i = 0
end = 0;
newstr = ""
index = 0
name = clubs[index]
while index < 20:
    if index == 18:
        print("duh")
    if name[i] == '-':
        name[i] = ' '



    if name[i:i+6] == "clubs/":
        i = i + 6
        while name[i] != "/":
            i = i + 1
        newstr = name[i+1:-1]
        newstr= newstr.replace('-' ,' ')## prints name rather cleanly
        print(newstr)
        index = index + 1
        name = clubs[index]
        i = 0
    else:
        i = i + 1







