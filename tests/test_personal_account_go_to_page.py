from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.locators import AfterRegistrationLocators
from src.data import get_exist_user_data
import time


class TestPersonalAccountPage:
    # Проверка перехода по клику на «Личный кабинет».
    def test_personal_account_go_to_page(self, driver, login):
        driver.find_element(*AfterRegistrationLocators.PERCONAL_ACCOUNT_BUTTON).click()
        time.sleep(3)
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(AfterRegistrationLocators.SAVE_BUTTON))
        element = driver.find_element(*AfterRegistrationLocators.SAVE_BUTTON).text
        assert driver.current_url == f"{Config.URL}/account/profile"
        assert element == "Сохранить"

