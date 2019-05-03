from locators.productPageLocators import ProductPageLocators as ppl
from page_objects.basePage import BasePage
import allure


class RightColumn(BasePage):

    add_to_cart = ppl.add_to_cart_xp
    layer_cart = ppl.layer_cart_xp
    close_layer_cart = ppl.close_layer_cart_xp
    shopping_cart = ppl.shopping_cart_xp
    remove_product_from_cart = ppl.remove_product_from_cart_xp
    cart_info = ppl.cart_info_xp

    def add_product_to_cart(self):
        self.click_clickable(self.add_to_cart)
        self.validate_element_present(self.layer_cart)

    def exit_layer_cart(self):
        self.click(self.close_layer_cart)

    def remove_from_dropdown_cart(self):
        self.hover(self.shopping_cart)
        self.click_clickable(self.remove_product_from_cart)
        self.driver.instance.find_elements_by_tag_name('a').size()

    def validate_cart_is_empty(self):
        if not self.wait(self.cart_info):
            print("Cart is empty")
            assert True
        else:
            print("Cart has not been cleared")
            assert False