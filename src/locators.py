from selenium.webdriver.common.by import By


class RegistrationLocators: #регистрация
    NAME_FIELD = By.XPATH, ".//label[text()='Имя']/following-sibling::input" #заполнение поля Имя
    EMAIL_FIELD = By.XPATH, ".//label[text()='Email']/following-sibling::input" #заполнение поля Email
    PASSWORD_FIELD = By.XPATH, './/input[@type="password"]' #заполнение поля Пароль
    REGISTRATION_BUTTON = By.XPATH, './/button[contains(@class,"button_button_type_primary")]' #кнопка "Зарегистрироваться
    LOGIN_BUTTON = By.XPATH, './/button[contains(@class,"button_button_type_primary")]' #кнопка "Войти"
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
    BUTGERS_PAGE = By.XPATH, ".//div[contains(@class, 'BurgerIngredients_ingredients__menuContainer')]" #отображение страницу с бургерами
    OFFERD = By.XPATH, './/button[contains(@class,"button_button_type_primary")]' #кнопка Оформить заказ

class AfterRegistrationLocators: #кнопки после атворизации в приложении
    PERCONAL_ACCOUNT_BUTTON = By.XPATH, ".//a[@href='/account']"  #кнопка Личный кабинет
    CONSTRUCTOR_BUTTON = By.XPATH, ".//a[contains(@class, 'AppHeader_header__link_active')]" #кнопка "Конструктор"
    LOGO = By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]" #логотип
    LOGOUT = By.XPATH, ".//button[@type='button' and text()='Выход']" #кнопка выход(на странице Личный кабинет)
    SAVE_BUTTON = By.XPATH, ".//button[contains(@class, 'button_button_type_primary')]" #кнопка Сохранить
    BUTGERS_PAGE = By.XPATH, ".//div[contains(@class, 'BurgerIngredients_ingredients__menuContainer')]" #отображение страницу с бургерами
    OFFERD = By.XPATH, './/button[contains(@class,"button_button_type_primary")]' #кнопка Оформить заказ
    LOGIN_BUTTON = By.XPATH, './/button[contains(@class,"button_button_type_primary")]' #кнопка "Войти"


class ConstructorLocators:
    BULKI = By.XPATH, ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']" #Раздел булки(активен)
    SAUCE = By.XPATH, "//div[@class = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Соусы']" #Раздел Соусы (раздел неактивен)
    GO_TO_SAUCE = By.XPATH, ".//div[contains(@class, 'current')]" #Добавлен current после перехода в раздел Соус
    NACHINKA = By.XPATH, "//div[@class = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Начинки']" #Раздел Начинки (раздел неактивен)
    GO_TO_NACHINKA = By.XPATH, ".//div[contains(@class, 'current')]" #Добавлен current после перехода в раздел Начинки
    BULKI_TITLE = By.XPATH, ".//h2[@class = 'text text_type_main-medium mb-6 mt-10' and text()='Булки']"
    SAUCE_TITLE = By.XPATH, ".//h2[@class = 'text text_type_main-medium mb-6 mt-10' and text()='Соусы']"
    NACHINKA_TITLE = By.XPATH, ".//h2[@class = 'text text_type_main-medium mb-6 mt-10' and text()='Начинки']"