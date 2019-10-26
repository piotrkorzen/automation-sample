from faker import Faker
from settings.webdriver import Driver
from page_objects.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.auth_page_locators import AuthLocators

"""Test to check whether each item in dropdown list can be selected"""


class TestAuth():

    def setup(self):
        self.driver = Driver()
        self.bp = BasePage(self.driver)
        fake = Faker()
        self.driver.navigate('http://automationpractice.com/index.php')
        self.bp.click(HomePageLocators.SIGN_IN)
        self.bp.set(AuthLocators.EMAIL_CREATE, fake.email())
        self.bp.click(AuthLocators.SUBMIT_CREATE)

    def test_days_dropdown(self):
        self.bp.get_items_from_dropdown(AuthLocators.DAYS)

        for item in self.bp.items:
            self.bp.validate_item_is_selected(AuthLocators.DAYS, item)

    def test_month_dropdown(self):
        self.bp.get_items_from_dropdown(AuthLocators.MONTHS)

        for item in self.bp.items:
            self.bp.validate_item_is_selected(AuthLocators.MONTHS, item)

    # def test_year_dropdown(self):
    #     self.bp.get_items_from_dropdown(AuthLocators.YEARS)
    #
    #     for item in self.bp.items:
    #         self.bp.validate_item_is_selected(AuthLocators.YEARS, item)

    def test_state_dropdown(self):
        self.bp.get_items_from_dropdown(AuthLocators.STATE)

        for item in self.bp.items:
            self.bp.validate_item_is_selected(AuthLocators.STATE, item)

    def teardown(self):
        self.driver.teardown()
