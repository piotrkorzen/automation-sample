from settings.webdriver import Driver
from page_objects.options_bar.checkboxes import *
import pytest

class TestCheckboxes():

    @pytest.fixture()
    def test_setup(self):
        self.driver = Driver()
        self.driver.navigate("http://automationpractice.com/index.php?id_category=3&controller=category")
        yield
        self.driver.instance.quit()

    def test_mark_checkboxes(self, test_setup):
        checkboxes = Checboxes(self.driver)
        checkboxes.click_size_checkboxes()
        checkboxes.click_composition_checkboxes()
        checkboxes.click_style_checkboxes()
        checkboxes.click_properties_checkboxes()
        checkboxes.click_availability_checkbox()
        checkboxes.click_manufacturer_checkbox()
        checkboxes.click_condition_checkbox()