from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def chromeDriver()->WebDriver:
    serv = Service(executable_path="driver\chromedriver.exe"
               ,log_path="reports\seleniumService.log")

    option = Options()
    # option.add_argument('--headless')
    option.add_argument('start-maximized')

    return WebDriver(options=option,service=serv)


