import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



@pytest.mark.ui
def test_check_incorrect_username():
    #Создание объекта для управления браузером
    driver = webdriver.Chrome(
        service = Service(r'C:\Users\User\QA_Automation_project\chromedriver.exe')
    )
    driver.get('https://github.com/login')

    login_elem = driver.find_element(By.ID, 'login_field')
    login_elem.send_keys('masterchief88')
    pass_element = driver.find_element(By.ID, 'password')
    pass_element.send_keys('ololololo')
    btn_elem = driver.find_element(By.NAME, 'commit')
    btn_elem.click()
    assert driver.title == 'Sign in to GitHub · GitHub'


    driver.close()


