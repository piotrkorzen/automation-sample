import pytest
import allure
from settings.webdriver import Driver
from page_objects.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class TestProductCart():

    @pytest.fixture()
    def test_setup(self):
        self.driver = Driver()
        self.bp = BasePage(self.driver)
        self.driver.navigate("http://automationpractice.com")
        yield
        self.driver.instance.quit()

    def test_add_to_cart_from_home_page(self, test_setup):
        self.bp.hover(HomePageLocators.ALL_PRODUCTS)
        self.bp.click_element(HomePageLocators.ADD_TO_CART)
        self.bp.validate_element_present(HomePageLocators.ICON_OK)

    def test_remove_from_cart(self, test_setup):
        self.test_add_to_cart_from_home_page(test_setup)
        self.bp.click(HomePageLocators.CLOSE_PRODUCT_LAYER)
        self.bp.hover(HomePageLocators.CART_VIEW)
        self.bp.click(HomePageLocators.RM_FROM_CART)
        self.bp.validate_element_present(HomePageLocators.EMPTY_CART_INFO)
