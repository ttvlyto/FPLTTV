from bs4 import BeautifulSoup
import asyncio
f = open("stats.txt", "r")
for line in f:
    newstr = f.read()
    break

soup = BeautifulSoup(newstr, "html.parser")
data = soup.find_all("div", {"class":"player-overview__info"})
moreData = soup.find_all("div", {"data-script":"pl_player"})
evenMoreData = soup.find("div", {"data-widget":"player-overview-stats"})
for x in data:
    print(x.get_text())

print("end ******")
for x in moreData:
    print(x)

print("end ******")
evenMoreData.getChild