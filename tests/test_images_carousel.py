from settings.webdriver import Driver
import pytest
from page_objects.home_page.categories import *
from page_objects.product_page.productImages import *
import time

class TestImagesCarousel():

    @pytest.fixture()
    def test_setup(self):
        self.driver = Driver()

        yield
        self.driver.instance.quit()

    def test_images_carousel(self, test_setup):
        self.prod = WomenCategoriesProducts(self.driver)
        self.image = ProductImages(self.driver)
        self.driver.navigate("http://automationpractice.com/index.php?id_category=3&controller=category")
        self.prod.click_product()
        self.image.show_all_images()