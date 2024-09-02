from selenium.webdriver.common.by import By


class RegistrationLocators: #регистрация
    #REGISTRATION_BUTTON = By.XPATH, ".//a[@href='/register']" #Кнопка "Зарегистрироваться (переход на заполнение регистрационных данных)"
    NAME_FIELD = By.XPATH, ".//label[text()='Имя']/following-sibling::input" #заполнение поля Имя
    EMAIL_FIELD = By.XPATH, ".//label[text()='Email']/following-sibling::input" #заполнение поля Email
    PASSWORD_FIELD = By.XPATH, './/input[@type="password"]' #заполнение поля Пароль
    REGISTRATION_BUTTON = By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]' #кнопка "Зарегистрироваться
    LOGIN_BUTTON = By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']" #кнопка "Войти"
    ERROR_PASSWORD = By.XPATH, ".//p[@class='input__error text_type_main-default']"


class LoginLocators: #вход по логин и паролю

    EMAIL_FIELD = By.XPATH, ".//input[@name='name']" #заполнение поля Email
    PASSWORD_FIELD = By.XPATH, ".//input[@name='Пароль']" #заполнение поля Пароль
    LOGIN_IN_ACCOUNT_BOTTON = By.XPATH, ".//button[text()='Войти в аккаунт']" #вход по кнопке «Войти в аккаунт» на главной
    LOGIN_PERCONAL_ACCOUNT_BUTTON = By.XPATH, ".//a[@href='/account']" #вход через кнопку «Личный кабинет»/кнопка Личный кабинет
    LOGIN_REGISTRATION_PAGE = By.CLASS_NAME, 'Auth_link__1fOlj'  # переход на страницу ввода email , password. "Войти" на станице регистрации
    PASSWORD_RECOVERY = By.XPATH, './/a[@href="/forgot-password"]' #кнопка востановить пароль
    LOGIN_RECOVERY_PAGE = By.XPATH, './/a[@href="/login"]' #вход через кнопку в форме восстановления пароля.
    LOGIN_BUTTON = By.XPATH, ".//button[text() = 'Войти']"
    BUTGERS_PAGE = By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']" #отображение страницу с бургерами
    OFFERD = By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']" #кнопка Оформить заказ

class AfterRegistrationLocators: #кнопки после атворизации в приложении
    PERCONAL_ACCOUNT_BUTTON = By.XPATH, ".//a[@href='/account']"  #кнопка Личный кабинет
    CONSTRUCTOR_BUTTON = By.XPATH, './/a[@href="/" and @class="AppHeader_header__link__3D_hX"]' #кнопка "Конструктор"
    LOGO = By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]" #логотип
    LOGOUT = By.XPATH, ".//button[@type='button' and text()='Выход']" #кнопка выход(на странице Личный кабинет)


class ConstructorLocators:
    BULKI = By.XPATH, './/span[text() = "Булки"]'
    SAUCE = By.XPATH, './/span[text() = "Соусы"]'
    NACHINKA = By.XPATH, './/span[text() = "Начинки"]'
    BULKI_TITLE = By.XPATH, ".//h2[@class = 'text text_type_main-medium mb-6 mt-10' and text()='Булки']"
    SAUCE_TITLE = By.XPATH, ".//h2[@class = 'text text_type_main-medium mb-6 mt-10' and text()='Соусы']"
    NACHINKA_TITLE = By.XPATH, ".//h2[@class = 'text text_type_main-medium mb-6 mt-10' and text()='Начинки']"




