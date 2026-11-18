from selenium.webdriver.support import expected_conditions as EC

from data import Urls
from locators import (ForgotPasswordPageLocators, HeaderLocators, LoginPageLocators,
                      MainPageLocators, RegisterPageLocators)


def fill_login_form(driver, wait, user):
    wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()


class TestLogin:

    def test_login_via_main_page_button(self, driver, wait, registered_user):
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)).click()
        fill_login_form(driver, wait, registered_user)

        assert wait.until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))

    def test_login_via_personal_account_button(self, driver, wait, registered_user):
        wait.until(EC.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_LINK)).click()
        fill_login_form(driver, wait, registered_user)

        assert wait.until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))

    def test_login_via_register_form_link(self, driver, wait, registered_user):
        driver.get(Urls.REGISTER)
        wait.until(EC.element_to_be_clickable(RegisterPageLocators.LOGIN_LINK)).click()
        fill_login_form(driver, wait, registered_user)

        assert wait.until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))

    def test_login_via_forgot_password_form_link(self, driver, wait, registered_user):
        driver.get(Urls.FORGOT_PASSWORD)
        wait.until(EC.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_LINK)).click()
        fill_login_form(driver, wait, registered_user)

        assert wait.until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
