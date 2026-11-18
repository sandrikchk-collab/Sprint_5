import pytest
from selenium.webdriver.support import expected_conditions as EC

from data import Urls
from locators import HeaderLocators, MainPageLocators, ProfilePageLocators


class TestAccountToConstructor:

    @pytest.mark.parametrize("locator", [HeaderLocators.CONSTRUCTOR_LINK, HeaderLocators.LOGO])
    def test_from_account_to_constructor(self, driver, wait, logged_in, locator):
        wait.until(EC.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_LINK)).click()
        wait.until(EC.visibility_of_element_located(ProfilePageLocators.PROFILE_LINK))

        driver.find_element(*locator).click()

        wait.until(EC.visibility_of_element_located(MainPageLocators.BURGER_HEADER))
        assert driver.current_url == Urls.MAIN
