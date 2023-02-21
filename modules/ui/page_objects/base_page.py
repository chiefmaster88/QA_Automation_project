from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BasePage:
    PATH = r'C:\Users\User\QA_Automation_project\chromedriver.exe'


    def __init__(self):
        self.driver = webdriver.Chrome(
            service = Service(BasePage.PATH)
        )


    def close(self):
        self.driver.close()

