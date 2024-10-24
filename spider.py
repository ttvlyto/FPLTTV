from bs4 import BeautifulSoup
import asyncio
from playwright.sync_api import sync_playwright
import time

html = ""
html2 = ""

link = "https://www.premierleague.com/players#!"

with sync_playwright() as p: ##launches browser using chromium
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(link)
    page.click("#onetrust-accept-btn-handler")
    close_advert_icon = page.get_by_role("link", name="Close Advert")

    # Ensure the element is visible and click it
    close_advert_icon.wait_for(state='visible', timeout=30000)
    close_advert_icon.click()


    page.wait_for_selector(".player")
    for x in range(1,500):
        page.keyboard.press("ArrowDown")
        time.sleep(.02)


    ##page.goto("https://www.premierleague.com/stats/top/players/goals") ## checks goals first


    html = page.content()
    ##print(html)
    ## page.goto("https://www.premierleague.com/clubs/") check clubs on list
    ##page.goto("https://www.premierleague.com/fixtures") ##broken ass fixtures
    ##context = browser.new_context()
    ##html2 = page.content()

    browser.close()

soup = BeautifulSoup(html, "html.parser")
table = soup.find_all("tr", {"class": "player"})
##print(table)
player = open("players.txt", "w")
for x in table:
    player.write(str(x) + "\n")
    print(str(x) + "\n")

player.close()

'''

##soup2 = BeautifulSoup(html2, "html.parser")
table = soup.find_all("tbody", {"class": "dataContainer indexSection"})
##clubs = soup2.find_all("li", {"class": "club-card-wrapper"})
##link = soup.find_all("href")
##clubs = (str)clubs
paragraphs = []
for x in clubs:
    paragraphs.append(str(x))

##print(paragraphs)



##print(soup.getText())
##for links in soup:

    ##print(links)






    i = i + 1
    ##print(string[i:i+4])
newstr = string[start:end + 10]
file = open("link.txt", 'a')
for x in ihatemyfuckinglife:
    file.write(x + "\n")
print(newstr)
'''




