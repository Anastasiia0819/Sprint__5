import pytest
from selenium import webdriver
from src.config import Config


#def browser_setting():
    #chrome_option = webdriver.ChromeOptions()
    #return chrome_option

@pytest.fixture
def driver():
    chrome = webdriver.Chrome() #(options=browser_setting)
    chrome.maximize_window()
    chrome.get(Config.URL)
    yield chrome
    chrome.quit()



