from settings.webdriver import Driver
from page_objects.basePage import BasePage
from locators.homePageLocators import HomePageLocators as hpl
import pytest
import allure


class TestProductCart():
    products = hpl.all_products
    add_to_cart = hpl.add_to_cart
    icon_ok = hpl.icon_ok
    close_product_layer = hpl.close_product_layer
    cart_view = hpl.cart_view
    rm_from_cart = hpl.rm_from_cart
    empty_cart_info = hpl.empty_cart_info

    @pytest.fixture()
    def test_setup(self):
        self.driver = Driver()
        self.bp = BasePage(self.driver)
        self.driver.navigate("http://automationpractice.com")
        yield
        self.driver.instance.quit()

    @allure.step("Add product to cart from home page")
    def test_add_to_cart_from_home_page(self, test_setup):
        self.bp.hover(self.products)
        self.bp.click_element(self.add_to_cart)
        self.bp.validate_element_present(self.icon_ok)

    @allure.step("Remove product from cart")
    def test_remove_from_cart(self, test_setup):
        self.test_add_to_cart_from_home_page(test_setup)
        self.bp.click(self.close_product_layer)
        self.bp.hover(self.cart_view)
        self.bp.click(self.rm_from_cart)
        self.bp.validate_element_present(self.empty_cart_info)
