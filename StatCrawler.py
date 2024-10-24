import asyncio
from playwright.sync_api import sync_playwright
import time
async def cookies():
    await page.click("#onetrust-accept-btn-handler")

stats = []
html = []
file = open("links.txt", "r")
for line in file:
    stats.append(line.strip())
with sync_playwright() as p: ##launches browser using chromium
    browser = p.chromium.launch(headless = False)
    page = browser.new_page()
    for x in range(0, 5):
        link = "https://" + stats[x]
        page.goto(link)
        context = browser.new_context()
        cookies()
        html.append(page.content())
        time.sleep(2)
    browser.close()

    f = open("stats.txt", "w")
    f.write(html[0])
    f.close()

