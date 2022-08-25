import asyncio
from playwright.async_api import async_playwright
import slack
import requests
import json
import os
list = []
isolated_en = []
isolated_ar = []
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://context.reverso.net/favourites/ezzz")
        await page.wait_for_timeout(3000)
        await page.locator("#results-length").click()
        await page.wait_for_timeout(1000)
        await page.locator(".option", has_text="50").click()
        await page.wait_for_timeout(2000)

        for i in range (1,40):
            example = await page.locator(f".examples >> nth={i}").inner_text()
            list.append(example)
        print(list)
        await browser.close()

asyncio.run(main())

for i in range(1,39):
   en_phrase = list[i].split("\n", 1)[0]
   isolated_en.append(en_phrase)
for i in range(1,39):
   ar_phrase = list[i].split("\n", 1)[1]
   isolated_ar.append(ar_phrase)
# isolated_en = dict[5].split("\n",1)[0]
# isolated_ar =dict[5].split("\n",1)[0]
# isolated_en.append(example).split("\n", 1)[0]
# isolated_ar.append(example).split("\n", 1)[1]

print(isolated_en)
print(isolated_ar)