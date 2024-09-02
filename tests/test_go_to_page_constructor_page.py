from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.locators import AfterRegistrationLocators
from src.data import get_exist_user_data
import time


class TestConstructorPage:
    # Проверка переход по клику на «Конструктор» и на логотип Stellar Burgers
    def test_constructor_go_to_page_from_personal_account_page(self, driver, login):
        driver.find_element(*AfterRegistrationLocators.PERCONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(AfterRegistrationLocators.SAVE_BUTTON))
        time.sleep(3)
        driver.find_element(*AfterRegistrationLocators.CONSTRUCTOR_BUTTON).click()

        time.sleep(3)
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(AfterRegistrationLocators.BUTGERS_PAGE))
        element = driver.find_element(*AfterRegistrationLocators.OFFERD).text
        assert element == "Оформить заказ"



