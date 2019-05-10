from page_objects.basePage import BasePage
from locators.homePageLocators import HomePageLocators as hpl
import allure

"""All items in home page header"""


class Header(BasePage):

    sign_in_xp = hpl.sign_in_xp

    @allure.step("Sign in button is clickable")
    def sign_in_button(self):
        self.click_clickable(self.sign_in_xp)