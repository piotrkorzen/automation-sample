from page_objects.basePage import BasePage
from locators.homePageLocators import HomePageLocators as hpl
import allure
import time

"""All products in home page"""

class Products(BasePage):

     product_xp = hpl.product_xp

     @allure.step("Sign in button is clickable")
     def sign_in_button(self):
         self.click_clickable(self.product_xp)