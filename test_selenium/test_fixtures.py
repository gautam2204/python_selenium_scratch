import pytest
from util.BaseDriver import chromeDriver
from selenium.webdriver.common.by import By

'''
Fixture without scope are called for every test and since it has yield it will also close every test
'''

@pytest.fixture()
def setThisasFixture():
    global driver
    driver = chromeDriver()
    yield
    driver.quit()
    

def test_1stCaseFromFixtture(setThisasFixture):
    driver.get("https://demoqa.com/automation-practice-form")
    elmHeading = driver.find_element(By.XPATH,"//div[@class='main-header']")
    assert "Practice Form"==elmHeading.text
    
def test_2ndCaseFromFixtture(setThisasFixture):
    driver.get("https://demoqa.com/automation-practice-form")
    elmHeading = driver.find_element(By.XPATH,"//div[@class='main-header']")
    assert "Practice Form"==elmHeading.text
 
 
def test_handle_window():
    driver.get("https://demoqa.com/browser-windows")
    