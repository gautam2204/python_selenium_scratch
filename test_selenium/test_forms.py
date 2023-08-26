from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from util.BaseDriver import chromeDriver
import pytest


def test_validateForm():
    driver = chromeDriver()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.set_page_load_timeout(10)   
    firstNameForm = driver.find_element(By.ID,"firstName")
    lastNameForm = driver.find_element(By.ID,"lastName")
    userEmailForm = driver.find_element(By.ID,"userEmail")
    userNumberForm = driver.find_element(By.ID,"userNumber")
    hobbiesWrapperForm = driver.find_element(By.ID,"hobbiesWrapper")
    # selectStateForm = driver.find_element(By.XPATH,"//div[contains(@class,'css-1pahdxg-control')]//div[contains(@class,'css-1hwfws3')]")
    submitButton = driver.find_element(By.ID,"submit")

    firstNameForm.send_keys("Gautam")
    lastNameForm.send_keys("rawat")
    action = ActionChains(driver)
    action.send_keys(Keys.TAB).send_keys("randomtest@gmail.hello").perform()
    userNumberForm.send_keys("8939725506")
    sleep(1)
    for i in range(1,4):
        elm = driver.find_element(By.ID,f'hobbies-checkbox-{i}')
        driver.execute_script("arguments[0].click();",elm)
        
    driver.execute_script("arguments[0].click();",submitButton)

def inc(a:int):
    return a+2

@pytest.mark.skip("Not related to selenium")
def test_validateSum():
    assert inc(3) == 5
    


