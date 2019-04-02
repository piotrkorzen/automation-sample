from settings.webdriver import Driver
import pytest
from page_objects.home_page.categories import *


class TestSortProducts():

    @pytest.fixture()
    def test_setup(self):
        self.driver = Driver()
        self.prod = WomenCategoriesProducts(self.driver)
        self.driver.navigate("http://automationpractice.com/index.php?id_category=3&controller=category")
        yield
        self.driver.instance.quit()

    def test_sort_by_price_asc(self, test_setup):
        self.prod.sort_by_price_highest_first()
        self.driver.instance.implicitly_wait(3)
        self.prod.validate_sort_asc(self.prod.get_product_price())

    def test_sort_by_price_desc(self, test_setup):
        self.prod.sort_by_price_lowest_first()

        self.driver.instance.implicitly_wait(3)
        self.prod.validate_sort_desc(self.prod.get_product_price())

    def test_sort_by_a_z(self, test_setup):
        self.prod.sort_by_name_a_to_z()

        self.driver.instance.implicitly_wait(3)
        self.prod.validate_sort_asc(self.prod.get_product_names())

    def test_sort_by_z_a(self, test_setup):
        self.prod.sort_by_name_z_to_a()

        self.driver.instance.implicitly_wait(3)
        self.prod.validate_sort_desc(self.prod.get_product_names())
