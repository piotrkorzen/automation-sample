from settings.webdriver import Driver
import os
import pytest
from page_objects.home_page.categories import *
from page_objects.auth_page.authPage import *
from data.dataGenerators import *
import time

class TestSortBy():

    @pytest.fixture()
    def test_setup(self):
        self.driver = Driver()
        yield
        self.driver.instance.quit()

    def test_sort_by(self, test_setup):
        self.driver.navigate("http://automationpractice.com/index.php?id_category=3&controller=category")

        prod = WomenCategoriesProducts(self.driver)
        prod.sort_by_price_highest_first()

        self.driver.instance.implicitly_wait(10)
        prod.validate_sort_products()