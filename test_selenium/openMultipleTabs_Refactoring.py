import asyncio
from bs4 import BeautifulSoup
from util.BaseDriver import chromeDriver

driver = chromeDriver()

MYTIAA_URL = "https://auth.tiaa.org/public/authentication/securelogin"


async def openTab(url: str):
    if (url.startswith("https")):
        openUrl = f"window.open('{url}','_blank')"
        driver.execute_script(openUrl)


async def enterUID_Pass(uid, passwrd):
    driver.execute_script("document.getElementById('userId').value='PH123456'")
    driver.execute_script("document.getElementById('password').value='1111111pP'")
    driver.execute_script("document.getElementById('form-submit-continue').click()")
    print(f"Final Results ={driver.page_source}")

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
    tasks = [openTab(url) for url in lst_of_final_urls]

    await asyncio.gather(*tasks)

    await enterUID_Pass("hello","123")


def quitBro():
    driver.quit()


asyncio.run(scrapPagetoGetAllUrls(),debug=True)
