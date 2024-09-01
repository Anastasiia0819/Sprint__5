from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.locators import RegistrationLocators
from src.data import get_exist_user_data
import time
from src.helpers import generate_password


class TestRegistration:

    def test_sign_up(self, driver):
        assert driver.current_url == f"{Config.URL}"

    #успешная регистрация
    def test_signup(self, driver):
        driver.get(f"{Config.URL}register") #переход на страницу регистрации
        time.sleep(2)
        email, password = get_exist_user_data()

        time.sleep(2)

         #ввод данных для регистрации
        driver.find_element(*RegistrationLocators.NAME_FIELD).send_keys("Анастасия")
        driver.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_FIELD).send_keys(password)

        time.sleep(2)

        #клик "Зарегистрироваться"
        driver.find_element(*RegistrationLocators.REGISTRATION_BUTTON).click()

        #дождаться пока кнопка "Войти" будет кликабельна
        login_button = WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(RegistrationLocators.LOGIN_BUTTON))
        time.sleep(2)
        assert driver.current_url == f"{Config.URL}login"

#Ошибка для некорректного пароля. Менее 6 символов в пароле
    def test_error_password(self, driver):
        driver.get(f"{Config.URL}register")  # переход на страницу регистрации
        password = generate_password(4)

    # ввод данных для регистрации
        driver.find_element(*RegistrationLocators.NAME_FIELD).send_keys("Анастасия")
        driver.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys("anastasiia@yandex.ru")
        driver.find_element(*RegistrationLocators.PASSWORD_FIELD).send_keys(password)

        time.sleep(2)

    # клик "Зарегистрироваться"
        driver.find_element(*RegistrationLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(RegistrationLocators.ERROR_PASSWORD))
        assert driver.find_element(*RegistrationLocators.ERROR_PASSWORD).text == "Некорректный пароль"

