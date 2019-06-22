from settings.webdriver import Driver
from page_objects.basePage import BasePage
from locators.categoriesLocators import CategoriesLocators as cl
import pytest
import allure

"""Test for checking whether checkboxes in left bar can be selected"""


class TestCheckboxes():
    checkboxes = cl.checkboxes

    @pytest.fixture()
    def test_setup(self):
        self.driver = Driver()
        self.bp = BasePage(self.driver)
        self.bp.driver.navigate("http://automationpractice.com/index.php?id_category=3&controller=category")
        yield
        self.bp.driver.instance.quit()

    @allure.step("All checkboxes on left side bar are clickable")
    def test_checkboxes(self, test_setup):
        all_checkboxes = self.driver.instance.find_elements_by_xpath(self.checkboxes)
        for checkbox in all_checkboxes:
            checkbox.click()
            assert checkbox.is_selected()
