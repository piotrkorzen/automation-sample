from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.productPageLocators import ProductPageLocators as ppl
from page_objects.basePage import BasePage
import allure


class RightColumn(BasePage):

    add_to_cart = ppl.add_to_cart_xp
    layer_cart = ppl.layer_cart_xp

    def add_product_to_cart(self):
        self.click_clickable(self.add_to_cart)
        self.validate_element_present(self.layer_cart)
