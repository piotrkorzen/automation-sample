from settings.webdriver import Driver
from locators.categoriesLocators import CategoriesLocators as cl
from page_objects.home_page.categories import Sort
import pytest


class TestSortProducts():
    sort_select = cl.sort_select
    prices = cl.prices
    product_name = cl.products_name

    @pytest.fixture()
    def test_setup(self):
        self.driver = Driver()
        self.s = Sort(self.driver)
        self.driver.navigate("http://automationpractice.com/index.php?id_category=3&controller=category")
        yield
        self.driver.instance.quit()

    def test_sort_by_price_asc(self, test_setup):
        self.s.set(self.sort_select, "Price: Lowest first")
        self.driver.instance.implicitly_wait(3)
        self.s.validate_sort_asc(self.s.get_product_price(self.prices))

    def test_sort_by_price_desc(self, test_setup):
        self.s.set(self.sort_select, "Price: Highest first")
        self.driver.instance.implicitly_wait(3)
        self.s.validate_sort_desc(self.s.get_product_price(self.prices))

    def test_sort_by_a_z(self, test_setup):
        self.s.set(self.sort_select, "Product Name: A to Z")
        self.driver.instance.implicitly_wait(3)
        self.s.validate_sort_asc(self.s.get_product_names(self.product_name))

    def test_sort_by_z_a(self, test_setup):
        self.s.set(self.sort_select, "Product Name: Z to A")
        self.driver.instance.implicitly_wait(3)
        self.s.validate_sort_desc(self.s.get_product_names(self.product_name))
