from selenium.webdriver.support import expected_conditions as EC

from data import Urls
from helpers import generate_password
from locators import LoginPageLocators, RegisterPageLocators


class TestRegistration:

    def test_registration_valid_data_redirects_to_login(self, driver, wait, new_user):
        driver.get(Urls.REGISTER)
        wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)).send_keys(new_user["name"])
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(new_user["email"])
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(new_user["password"])
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        wait.until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_HEADER))
        assert driver.current_url == Urls.LOGIN

    def test_registration_short_password_shows_error(self, driver, wait, new_user):
        driver.get(Urls.REGISTER)
        wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)).send_keys(new_user["name"])
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(new_user["email"])
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(generate_password(5))
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        error = wait.until(EC.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR))
        assert error.text == "Некорректный пароль"
