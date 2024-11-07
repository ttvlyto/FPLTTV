from bs4 import BeautifulSoup
import asyncio


f = open("links.txt", "r")
p = open("playerStats.txt", "w")
def parseStats(stats, len): ## passes thru dict with link and keyPair html 
    name = '' 
    club = ''
    dob = ''
    appearances = 0
    arr = []

    for line in f:

        p.write(line + '\n')
        #######
        newstr = line
        newstr = newstr[35:-10]
        if newstr[0].isdigit():
            newstr = newstr[2:]
    
        elif newstr[0] == '/':
            newstr = newstr[1:]
    
        newstr = newstr.replace('-', ' ')

        p.write(newstr + '\n')
    
        ######
        newstr = (stats[line])
        p.write(newstr + '\n')
        soup = BeautifulSoup(newstr, "html.parser")
        data = soup.find_all("div", {"class": "player-overview__info"})
        moreData = soup.find_all("div", {"data-script": "pl_player"})
        evenMoreData = soup.find("div", {"data-widget": "player-overview-stats"})
        index = 0
        for x in data:
            print(index, ". HTML")
            p.write(x.prettify())
            print(x.get_text())
            index += 1


        p.write("******end, new player******\n")




    ##evenMoreData.getChild
