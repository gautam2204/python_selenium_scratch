import pytest
from util.BaseDriver import chromeDriver
from selenium.webdriver.common.by import By

'''
Fixture with scope are called at start of first test and since it has yield it will
close at the completion of last test 
'''

@pytest.fixture(scope="module")
def setThisasFixtureWithScope():
    global driver
    driver = chromeDriver()
    yield
    driver.quit()
    

def test_1stCaseFromFixttureWithScope(setThisasFixtureWithScope):
    driver.get("https://demoqa.com/automation-practice-form")
    elmHeading = driver.find_element(By.XPATH,"//div[@class='main-header']")
    assert "Practice Form"==elmHeading.text
    
def test_2stCaseFromFixttureWithScope(setThisasFixtureWithScope):
    driver.get("https://demoqa.com/text-box")
    elmHeading = driver.find_element(By.XPATH,"//div[@class='main-header']")
    assert "Text Box"==elmHeading.text
 