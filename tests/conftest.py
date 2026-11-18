import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import Urls, UserData, WAIT_TIMEOUT
from helpers import generate_email, generate_password
from locators import LoginPageLocators, MainPageLocators, RegisterPageLocators


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=options)
    browser.get(Urls.MAIN)
    yield browser
    browser.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, WAIT_TIMEOUT)


@pytest.fixture
def new_user():
    """Данные нового пользователя (сгенерированные логин и пароль)."""
    return {"name": UserData.NAME, "email": generate_email(), "password": generate_password()}


@pytest.fixture
def registered_user(driver, wait, new_user):
    """Регистрирует пользователя через UI и возвращает его данные."""
    driver.get(Urls.REGISTER)
    wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)).send_keys(new_user["name"])
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(new_user["email"])
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(new_user["password"])
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    wait.until(EC.url_to_be(Urls.LOGIN))
    driver.get(Urls.MAIN)
    return new_user


@pytest.fixture
def logged_in(driver, wait, registered_user):
    """Авторизует зарегистрированного пользователя и оставляет его на главной."""
    driver.get(Urls.LOGIN)
    wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(registered_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    wait.until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
    return registered_user
