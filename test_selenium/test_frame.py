import time
import pytest
from util.BaseDriver import chromeDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import logging


@pytest.fixture()
def setThisasFixtureFrame():
    global driver
    driver = chromeDriver()
    logging.info("[Since No scope mentioned yield will be executed everytime post end of test]")
    yield
    driver.quit()
    
def test_handle_multipleFrames(setThisasFixtureFrame):
    driver.get("https://demoqa.com/frames")
    frame_list = driver.find_elements(By.XPATH,"//iframe[@src='/sample']")
    time.sleep(3)
    for frame in frame_list:        
        driver.execute_script("arguments[0].scrollIntoView(true);", frame)
        driver.switch_to.frame(frame)
        element_in_frame = driver.find_element(By.XPATH,"//*[@id='sampleHeading']")
        print(element_in_frame.text)
        driver.switch_to.default_content()
        
        

        
        
        
