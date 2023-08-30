import time
import pytest
from util.BaseDriver import chromeDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


@pytest.fixture()
def setThisasFixture():
    global driver
    driver = chromeDriver()
    yield
    driver.quit()
    
def test_handle_newTab(setThisasFixture):
    driver.get("https://demoqa.com/browser-windows")
    elm = driver.find_element(By.ID,"tabButton")
    elm.click()
    time.sleep(3)
    handles = driver.window_handles
    for handle in handles:
        driver.switch_to.window(handle)
        print(driver.current_url)
        
   
def test_handle_newWindow(setThisasFixture):
    driver.get("https://demoqa.com/browser-windows")
    elm = driver.find_element(By.ID,"windowButton")
    elm.click()
    time.sleep(3)
    handles = driver.window_handles
    for handle in handles:
        driver.switch_to.window(handle)
        print(driver.current_url)
     
def test_handle_newMessageWindow(setThisasFixture):
    driver.get("https://demoqa.com/browser-windows")
    elm = driver.find_element(By.XPATH,"//*[@id='msgWindowButtonWrapper']/button")
    driver.execute_script("arguments[0].scrollIntoView(true);", elm)
    driver.execute_script("arguments[0].click();",elm)
    time.sleep(3)
    parent_window = driver.current_window_handle
    handles = driver.window_handles
    for handle in handles:
        try:            
            if not (handle==parent_window):
                '''driver.switch_to.window(handle)
                print("Since url is blank will use focus ")
                driver.get("https://demoqa.com/alerts")
                # wait = WebDriverWait(driver, 10)
                # elmm = wait.until(EC.visibility_of_any_elements_located(driver.find_elements(By.XPATH, "//body")))
                

                print(f"Text in Url is = {driver.title}")'''
        except TimeoutError as e:
            e.with_traceback()        
        
 