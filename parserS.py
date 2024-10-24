from bs4 import BeautifulSoup
import asyncio
f = open("stats.txt", "r")
def parseStats(stats, len):

    for x in range(0,len):
        newstr = stats[x]
        soup = BeautifulSoup(newstr, "html.parser")
        data = soup.find_all("div", {"class": "player-overview__info"})
        moreData = soup.find_all("div", {"data-script": "pl_player"})
        evenMoreData = soup.find("div", {"data-widget": "player-overview-stats"})
        for x in data:
            print(x.get_text())

        print("end ******")
        for x in moreData:
            print(x.get_text())

        print("end ******")


    ##evenMoreData.getChild