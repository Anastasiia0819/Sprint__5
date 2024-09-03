from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.locators import ConstructorLocators
import time

#Проверка, что работают переходы к разделам: «Булки», «Соусы», «Начинки»
class TestConstructionGoChapter:
    def test_go_chapter_bulki(self, driver, login):
        assert driver.find_element(*ConstructorLocators.BULKI)

    def test_go_chapter_sauce(self, driver, login):
        driver.find_element(*ConstructorLocators.SAUCE).click()
        time.sleep(3)
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(ConstructorLocators.SAUCE_TITLE))
        sauce_title = driver.find_element(*ConstructorLocators.SAUCE_TITLE)
        assert driver.find_element(*ConstructorLocators.GO_TO_SAUCE)
        assert sauce_title.is_displayed() #Заголовок Соусы виден на странице

    def test_go_chapter_nachinka(self, driver, login):
        driver.find_element(*ConstructorLocators.NACHINKA).click()
        time.sleep(3)
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(ConstructorLocators.NACHINKA_TITLE))
        sauce_title = driver.find_element(*ConstructorLocators.NACHINKA_TITLE)
        assert driver.find_element(*ConstructorLocators.GO_TO_NACHINKA)
        assert sauce_title.is_displayed()  # Заголовок Соусы виден на странице




