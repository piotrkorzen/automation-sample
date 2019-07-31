from settings.webdriver import Driver
from page_objects.base_page import BasePage
from locators.categories_locators import CategoriesLocators

"""Test to check whether checkboxes in left column can be selected"""


class TestCheckboxes():

    def setup(self):
        self.driver = Driver()
        self.bp = BasePage(self.driver)
        self.bp.driver.navigate("http://automationpractice.com/index.php?id_category=3&controller=category")

    def test_checkboxes(self):
        all_checkboxes = self.driver.instance.find_elements(*self.bp.locator(CategoriesLocators.CHECKBOXES))
        for checkbox in all_checkboxes:
            checkbox.click()
            assert checkbox.is_selected()

    def teardown(self):
        self.bp.driver.instance.quit()
