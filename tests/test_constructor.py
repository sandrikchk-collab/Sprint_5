from selenium.webdriver.support import expected_conditions as EC

from locators import ConstructorLocators


class TestConstructor:

    def test_buns_tab_becomes_active(self, driver, wait):
        # «Булки» активна по умолчанию, поэтому сначала уходим на другую вкладку
        wait.until(EC.element_to_be_clickable(ConstructorLocators.SAUCES_TAB)).click()
        driver.find_element(*ConstructorLocators.BUNS_TAB).click()

        wait.until(EC.text_to_be_present_in_element(ConstructorLocators.ACTIVE_TAB, "Булки"))
        assert driver.find_element(*ConstructorLocators.ACTIVE_TAB).text == "Булки"

    def test_sauces_tab_becomes_active(self, driver, wait):
        wait.until(EC.element_to_be_clickable(ConstructorLocators.SAUCES_TAB)).click()

        wait.until(EC.text_to_be_present_in_element(ConstructorLocators.ACTIVE_TAB, "Соусы"))
        assert driver.find_element(*ConstructorLocators.ACTIVE_TAB).text == "Соусы"

    def test_fillings_tab_becomes_active(self, driver, wait):
        wait.until(EC.element_to_be_clickable(ConstructorLocators.FILLINGS_TAB)).click()

        wait.until(EC.text_to_be_present_in_element(ConstructorLocators.ACTIVE_TAB, "Начинки"))
        assert driver.find_element(*ConstructorLocators.ACTIVE_TAB).text == "Начинки"
