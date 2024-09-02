from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.locators import AfterRegistrationLocators
import time
from src.config import Config


class TestLogout:
    # Проверка выхода по кнопке «Выйти» в личном кабинете
    def test_constructor_go_to_page_from_personal_account_page(self, driver, login):
        driver.find_element(*AfterRegistrationLocators.PERCONAL_ACCOUNT_BUTTON).click() #клик на Личный кабинет
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(AfterRegistrationLocators.LOGOUT))

        time.sleep(3)
        driver.find_element(*AfterRegistrationLocators.LOGOUT).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(AfterRegistrationLocators.LOGIN_BUTTON))
        time.sleep(3)
        assert driver.current_url == f"{Config.URL}/login"
