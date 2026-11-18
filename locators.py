from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка «Оформить заказ» (видна только авторизованному)
    BURGER_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок «Соберите бургер» в конструкторе


class HeaderLocators:
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка «Личный Кабинет» в шапке
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка «Конструктор» в шапке
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]/a")  # Логотип Stellar Burgers в шапке


class LoginPageLocators:
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")  # Заголовок «Вход» формы входа
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")  # Поле «Email» на форме входа
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # Поле «Пароль» на форме входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка «Войти» на форме входа
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Ссылка «Зарегистрироваться»
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # Ссылка «Восстановить пароль»


class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле «Имя»
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле «Email»
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # Поле «Пароль»
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка «Зарегистрироваться»
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")  # Ошибка «Некорректный пароль»
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка «Войти» под формой регистрации


class ForgotPasswordPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка «Войти» на форме восстановления пароля


class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")  # Вкладка «Профиль» в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка «Выход» в личном кабинете


class ConstructorLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")  # Вкладка «Булки»
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")  # Вкладка «Соусы»
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")  # Вкладка «Начинки»
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/span")  # Текст активной вкладки
