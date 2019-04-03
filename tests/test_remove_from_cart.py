from settings.webdriver import Driver
import pytest
from page_objects.home_page.categories import *
from page_objects.product_page.productPage import *
import time

class TestProductCart():


    @pytest.fixture()
    def test_setup(self):
        self.driver = Driver()
        self.prod = WomenCategoriesProducts(self.driver)
        self.pp = RightColumn(self.driver)
        self.driver.navigate("http://automationpractice.com/index.php?id_category=3&controller=category")
        yield
        self.driver.instance.quit()

    def test_add_faded_short_sleeve(self, test_setup):
        self.prod.click_product(2)
        self.pp.add_product_to_cart()

        time.sleep(3)