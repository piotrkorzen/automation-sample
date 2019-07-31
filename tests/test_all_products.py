from settings.webdriver import Driver
from page_objects.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.product_page_locators import ProductPageLocators


class TestImagesCarousel():

    def setup(self):
        self.driver = Driver()
        self.bp = BasePage(self.driver)
        self.driver.navigate("http://automationpractice.com/index.php?id_category=3&controller=category")
        products = self.driver.instance.find_elements_by_xpath(HomePageLocators.ALL_PRODUCTS)
        self.product_links = []
        # Get all links to product in particular category
        for link in products:
            full_link = link.get_attribute('href')
            self.product_links.append(full_link)

    def test_images_carousel(self):
        """navigate to product one by one"""
        for href in self.product_links:
            self.driver.navigate(href)
            images = self.driver.instance.find_elements_by_xpath(ProductPageLocators.IMAGE_LST)
            for image in images:
                image.click()
                self.bp.validate_element_present(ProductPageLocators.IMAGE_BOX)
                self.bp.click(ProductPageLocators.CLOSE_PRODUCT_IMAGE)
                self.bp.validate_element_not_present(ProductPageLocators.IMAGE_LAYER)

    def test_socials_are_visible(self):
        """navigate to product one by one"""
        for href in self.product_links:
            self.driver.navigate(href)
            self.bp.validate_element_present(ProductPageLocators.TWITTER)
            self.bp.validate_element_present(ProductPageLocators.FACEBOOK)
            self.bp.validate_element_present(ProductPageLocators.GOOGLE_PLUS)
            self.bp.validate_element_present(ProductPageLocators.PINTEREST)

    def teardown(self):
        self.driver.instance.quit()
