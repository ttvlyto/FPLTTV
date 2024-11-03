from bs4 import BeautifulSoup
import asyncio
f = open("stats.txt", "r")
p = open("playerStats.txt", "w")
def parseStats(stats, len):
    name = ''
    club = ''
    dob = ''
    appearances = 0
    arr = []

    for x in range(0,len):
        newstr = stats[x]
        soup = BeautifulSoup(newstr, "html.parser")
        data = soup.find_all("div", {"class": "player-overview__info"})
        moreData = soup.find_all("div", {"data-script": "pl_player"})
        evenMoreData = soup.find("div", {"data-widget": "player-overview-stats"})
        index = 0
        for x in data:
            print(index, ". HTML")
            arr.append(x.prettify())
            print(x.prettify())
            print("TEXT")
            print(x.get_text())
            index += 1


        print("end ******")

    for x in arr:
        p.write(x)


        i = 0
        start = 0
        end = 0
        while i < 4000:
            if newstr[i:i+14] == "overview__info":
                start = i
                while newstr[i] != "<":
                    i += 1
                end = i
            else:
                i += 1

        print(newstr[start:end])
        continue


        index = 0
        '''
        for x in moreData:
            print(index, '. HTML')
            print(x.prettify())

            print("TEXT")
            print(x.get_text())
            index += 1
        '''
    print("end ******")


    ##evenMoreData.getChild