from selenium.webdriver.support import expected_conditions as EC

from data import Urls
from locators import HeaderLocators, LoginPageLocators, ProfilePageLocators


class TestLogout:

    def test_logout_from_personal_account(self, driver, wait, logged_in):
        wait.until(EC.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_LINK)).click()
        wait.until(EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_HEADER))
        assert driver.current_url == Urls.LOGIN
