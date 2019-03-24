from settings.webdriver import Driver
import os
import pytest
from page_objects.home_page.categories import *
from page_objects.auth_page.authPage import *
from data.dataGenerators import *
import time

class TestSortProducts():

    @pytest.fixture()
    def test_setup(self):
        self.driver = Driver()
        self.driver.navigate("http://automationpractice.com/index.php?id_category=3&controller=category")
        yield
        self.driver.instance.quit()

    def test_sort_by_price_asc(self, test_setup):
        prod = WomenCategoriesProducts(self.driver)
        prod.sort_by_price_highest_first()

        self.driver.instance.implicitly_wait(10)
        prod.validate_sort_asc(prod.get_product_price())

    def test_sort_by_price_desc(self, test_setup):
        prod = WomenCategoriesProducts(self.driver)
        prod.sort_by_price_highest_first()

        self.driver.instance.implicitly_wait(10)
        prod.validate_sort_desc(prod.get_product_price())

    def test_sort_by_A_Z(self, test_setup):
        prod = WomenCategoriesProducts(self.driver)
        prod.sort_by_price_highest_first()

        self.driver.instance.implicitly_wait(10)
        prod.validate_sort_asc(prod.get_product_names())

    def test_sort_by_Z_A(self, test_setup):
        prod = WomenCategoriesProducts(self.driver)
        prod.sort_by_price_highest_first()

        self.driver.instance.implicitly_wait(10)
        prod.validate_sort_desc(prod.get_product_names())