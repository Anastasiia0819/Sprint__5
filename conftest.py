import pytest
from selenium import webdriver
from src.config import Config
from src.locators import LoginLocators
from src.data import get_exist_user_data
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver():
    chrome = webdriver.Chrome() #(options=browser_setting)
    chrome.maximize_window()
    chrome.get(Config.URL)
    yield chrome
    chrome.quit()


@pytest.fixture
def login(driver):
    driver.get(f"{Config.URL}login")
    email, password = get_exist_user_data()
    driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys(email)  # заполнить поле почта
    driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(password)  # заполнить поле пароль
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()  # клик на Войти
    assert driver.current_url == f"{Config.URL}login"
    WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(LoginLocators.BUTGERS_PAGE))
    element = driver.find_element(*LoginLocators.OFFERD)
    time.sleep(3)
    assert element.is_displayed()
    assert element.is_enabled()




