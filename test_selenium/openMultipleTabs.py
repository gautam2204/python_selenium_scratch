import asyncio
from bs4 import BeautifulSoup
from util.BaseDriver import chromeDriver

driver = chromeDriver()

MYTIAA_URL = "https://auth.tiaa.org/public/authentication/securelogin"


async def openTab(url: str):
    if (url.startswith("https")):
        openUrl = f"window.open('{url}','_blank')"
        driver.execute_script(openUrl)


async def scrapPagetoGetAllUrls():
    driver.get(MYTIAA_URL)
    pageSource = driver.page_source
    soup = BeautifulSoup(pageSource, 'html.parser')
    print(soup)
    anchor_tags = soup.select('a')
    lst_of_final_urls = []
    for link in anchor_tags:
        link_to_open = str(link.get('href'))
        if not 'None' in link_to_open and 'https' in link_to_open:
            lst_of_final_urls.append(link_to_open)

    print(f'{lst_of_final_urls} and count is {len(lst_of_final_urls)}')

    list_of_page_title = []
    for url in lst_of_final_urls:
        task = await asyncio.create_task(openTab(url))



    print(list_of_page_title)
    driver.quit()


asyncio.run(scrapPagetoGetAllUrls())
