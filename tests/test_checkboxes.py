import pytest
import allure
from settings.webdriver import Driver
from page_objects.base_page import BasePage
from locators.categories_locators import CategoriesLocators

"""Test to check whether checkboxes in left column can be selected"""


class TestCheckboxes():

    @pytest.fixture()
    def test_setup(self):
        self.driver = Driver()
        self.bp = BasePage(self.driver)
        self.bp.driver.navigate("http://automationpractice.com/index.php?id_category=3&controller=category")
        yield
        self.bp.driver.instance.quit()

    @allure.step("All checkboxes on left side bar are clickable")
    def test_checkboxes(self, test_setup):
        all_checkboxes = self.driver.instance.find_elements_by_xpath(CategoriesLocators.CHECKBOXES)
        for checkbox in all_checkboxes:
            checkbox.click()
            assert checkbox.is_selected()
