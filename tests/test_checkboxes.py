from settings.webdriver import Driver
from page_objects.options_bar.catalog import *
import pytest
import time
class TestCheckboxes():

    @pytest.fixture()
    def test_setup(self):
        self.driver = Driver()
        self.driver.navigate("http://automationpractice.com/index.php?id_category=3&controller=category")
        yield
        self.driver.instance.quit()

    def test_mark_checkboxes(self, test_setup):
        checkboxes = Checboxes(self.driver)
        checkboxes.price_slider()
        time.sleep(5)