from selenium.webdriver.support import expected_conditions as EC

from data import Urls
from locators import HeaderLocators, ProfilePageLocators


class TestPersonalAccount:

    def test_personal_account_link_opens_profile(self, driver, wait, logged_in):
        wait.until(EC.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_LINK)).click()

        wait.until(EC.visibility_of_element_located(ProfilePageLocators.PROFILE_LINK))
        assert driver.current_url == Urls.PROFILE
