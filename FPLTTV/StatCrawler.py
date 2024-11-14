
import time
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import parserS
import testerfile

stats = []
html = []
keyPairs = {}
statsFile = open('playerStats.txt', 'w')

file = open("links.txt", "r") ## opens list of player overview links from prem official site
for line in file: ## redundatly adding files in list
    stats.append(line)

with sync_playwright() as p: ##launches browser using chromium
    browser = p.chromium.launch(headless = False)
    page = browser.new_page()
    for x in range(0, 997): ##iterate through player links
        link = "https://" + stats[x] 
        page.goto(link)
        context = browser.new_context()
        ##handelers for cookies and ads
        try:
            page.click("#onetrust-accept-btn-handler", timeout=100)
        except PlaywrightTimeoutError:
            print("No cookies")

        try:
            close_advert_icon = page.get_by_role("link", name="Close Advert")
            close_advert_icon.wait_for(state='visible', timeout=500)
            close_advert_icon.click()
        except PlaywrightTimeoutError:
            print("no advert to close")

        player_HTML = page.content()
        print(f'Current Player: {stats[x]}') ##fancy print which player we are on
        print("writing html to txt")


        html.append(player_HTML) ##finally add source html to list
        keyPairs[stats[x]] = player_HTML
        statsFile.write('Player link: ' + stats[x] + '\n')
        statsFile.write(player_HTML)
        statsFile.write("******end, new player******\n")
        



        time.sleep(1)
    browser.close()
listlen = len(keyPairs)







parserS.testParser() ##pare html in separate tab
testerfile.parseNprint()

