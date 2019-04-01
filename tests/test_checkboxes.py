from settings.webdriver import Driver
from page_objects.options_bar.catalog import *
import pytest
import time

"""Tests for checking whether checkboxes in left bar are clickable"""

class TestCheckboxes():

    @pytest.fixture()
    def test_setup(self):
        self.driver = Driver()
        self.checkboxes = Checboxes(self.driver)
        self.driver.navigate("http://automationpractice.com/index.php?id_category=3&controller=category")
        yield
        time.sleep(3)
        self.driver.instance.quit()

    def test_mark_categories(self, test_setup):
        self.checkboxes.click_categories_checkboxes()

    def test_mark_size(self, test_setup):
        self.checkboxes.click_size_checkboxes()

    def test_mark_color(self, test_setup):
        self.checkboxes.click_color_checkboxes()

    def test_mark_composition(self, test_setup):
        self.checkboxes.click_composition_checkboxes()

    def test_mark_style(self, test_setup):
        self.checkboxes.click_style_checkboxes()

    def test_mark_properties(self, test_setup):
        self.checkboxes.click_properties_checkboxes()

    def test_mark_availability(self, test_setup):
        self.checkboxes.click_availability_checkbox()

    def test_mark_manufacturer(self, test_setup):
        self.checkboxes.click_manufacturer_checkbox()

    def test_mark_condition(self, test_setup):
        self.checkboxes.click_condition_checkbox()

