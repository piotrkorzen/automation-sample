from settings.webdriver import Driver
from page_objects.basePage import BasePage
from locators.homePageLocators import HomePageLocators as hpl
from locators.productPageLocators import ProductPageLocators as ppl
import pytest
import allure


class TestImagesCarousel():
    image_lst = ppl.image_lst_xp
    image_box = ppl.image_box
    close_image = ppl.close_product_image
    image_layer = ppl.image_layer
    products = hpl.all_products
    twitter = ppl.twitter
    facebook = ppl.facebook
    google_plus = ppl.google_plus
    pinterest = ppl.pinterest

    @pytest.fixture()
    def test_setup(self):
        self.driver = Driver()
        self.bp = BasePage(self.driver)
        self.driver.navigate("http://automationpractice.com/index.php?id_category=3&controller=category")
        products = self.driver.instance.find_elements_by_xpath(self.products)
        self.product_links = []
        # Get all links to product in particular category
        for link in products:
            full_link = link.get_attribute('href')
            self.product_links.append(full_link)
        yield
        self.driver.instance.quit()

    @allure.step("Check whether large view of products pictures is possible")
    def test_images_carousel(self, test_setup):
        # navigate to product one by one
        for href in self.product_links:
            self.driver.navigate(href)
            images = self.driver.instance.find_elements_by_xpath(self.image_lst)
            for image in images:
                image.click()
                self.bp.validate_element_present(self.image_box)
                self.bp.click(self.close_image)
                self.bp.validate_element_not_present(self.image_layer)

    @allure.step("Check whether socials buttons are visible")
    def test_socials_are_visible(self, test_setup):
        # navigate to product one by one
        for href in self.product_links:
            self.driver.navigate(href)
            self.bp.validate_element_present(self.twitter)
            self.bp.validate_element_present(self.facebook)
            self.bp.validate_element_present(self.google_plus)
            self.bp.validate_element_present(self.pinterest)
