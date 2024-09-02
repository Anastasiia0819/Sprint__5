from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.locators import LoginLocators
from src.data import get_exist_user_data
import time


class TestLogin:

    #вход по кнопке «Войти в аккаунт» на главной
    def test_login_login_in_account(self, driver):
        driver.find_element(*LoginLocators.LOGIN_IN_ACCOUNT_BOTTON).click() #клик на Войти в аккаунт
        time.sleep(2)
        email, password = get_exist_user_data()
        assert driver.current_url == f"{Config.URL}/login"

        driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys(email) #заполнить поле почта
        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(password) #заполнить поле пароль
        time.sleep(2)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click() #клик на Войти

        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(LoginLocators.BUTGERS_PAGE))
        element = driver.find_element(*LoginLocators.OFFERD)
        assert element.is_displayed()
        assert element.is_enabled()

    #вход через кнопку «Личный кабинет»
    def test_login_personal_account(self, driver):
        driver.find_element(*LoginLocators.LOGIN_PERCONAL_ACCOUNT_BUTTON).click() #клик на Личный кабинет
        time.sleep(3)
        email, password = get_exist_user_data()
        assert driver.current_url == f"{Config.URL}/login"

        driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys(email)  # заполнить поле почта
        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(password)  # заполнить поле пароль
        time.sleep(2)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()  # клик на Войти

        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(LoginLocators.BUTGERS_PAGE))
        element = driver.find_element(*LoginLocators.OFFERD)
        time.sleep(3)
        assert element.is_displayed()
        assert element.is_enabled()


    #вход через кнопку в форме регистрации
    def test_login_form_registation_page(self, driver):
        driver.get(f"{Config.URL}/register")
        driver.find_element(*LoginLocators.LOGIN_REGISTRATION_PAGE).click()#клик на кнопку зарегистрироваться
        time.sleep(3)
        email, password = get_exist_user_data()
        assert driver.current_url == f"{Config.URL}/login"

        driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys(email)  # заполнить поле почта
        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(password)  # заполнить поле пароль
        time.sleep(2)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()  # клик на Войти

        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(LoginLocators.BUTGERS_PAGE))
        element = driver.find_element(*LoginLocators.OFFERD)
        time.sleep(3)
        assert element.is_displayed()
        assert element.is_enabled()



    #вход через кнопку в форме восстановления пароля
    def test_login_password_recovery_page(self, driver):
        driver.get(f"{Config.URL}/forgot-password")
        driver.find_element(*LoginLocators.LOGIN_RECOVERY_PAGE).click()  # клик на кнопку зарегистрироваться
        time.sleep(3)
        email, password = get_exist_user_data()
        assert driver.current_url == f"{Config.URL}/login"

        driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys(email)  # заполнить поле почта
        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(password)  # заполнить поле пароль
        time.sleep(2)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()  # клик на Войти

        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(LoginLocators.BUTGERS_PAGE))
        element = driver.find_element(*LoginLocators.OFFERD)
        time.sleep(3)
        assert element.is_displayed()
        assert element.is_enabled()
