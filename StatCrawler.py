import asyncio
from playwright.sync_api import sync_playwright
import time
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import parserS
async def cookies():
    await page.click("#onetrust-accept-btn-handler")
    closeAd = page.get_by_role("link", name="Close Advert")
    await closeAd.wait_for(state="visable", timeout=30000)
    await closeAd.click()



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
        try:
            page.click("#onetrust-accept-btn-handler", timeout=100)
        except PlaywrightTimeoutError:
            print("No cookies")




        html.append(page.content())
        time.sleep(2)
    browser.close()
    len = len(html)

parserS.parseStats(html, len)

