import os
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def deleteFilesinReports(directory):
    file_list=os.listdir(directory)
    for file_name in file_list:
        file_path = os.path.join(directory, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                print(f"Skipping non-file item: {file_name}")
        except Exception as e:
            print(f"Error deleting {file_name}: {e}")

def chromeDriver()->WebDriver:
    log_directory = "reports"

    # Create the log directory if it doesn't exist
    os.makedirs(log_directory, exist_ok=True)
    deleteFilesinReports(log_directory)
    # Create a unique log file name for each execution
    log_file_name = "seleniumService_{}.log".format("updateScenarioNameLater")  # Use a unique identifier

    # Full path to the log file
    log_path = os.path.join(log_directory, log_file_name)
    serv = Service(executable_path="driver\chromedriver.exe"
               ,log_output=log_path
               ,)

    option = Options()
    # option.add_argument('--headless')
    option.add_argument('start-maximized')

    return WebDriver(options=option,service=serv)


