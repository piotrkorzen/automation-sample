from settings.webdriver import Driver
from page_objects.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.auth_page_locators import AuthLocators
from faker import Faker
import pytest
import allure

"""Test to check whether each item in dropdown list can be selected"""


class TestAuth():

    @pytest.fixture()
    def test_setup(self):
        self.driver = Driver()
        self.bp = BasePage(self.driver)
        fake = Faker()
        self.driver.navigate('http://automationpractice.com/index.php')
        self.bp.click(HomePageLocators.SIGN_IN)
        self.bp.set(AuthLocators.EMAIL_CREATE, fake.email())
        self.bp.click(AuthLocators.SUBMIT_CREATE)
        yield
        self.driver.instance.quit()

    @allure.step("Each item from days dropdown can be selected")
    def test_days_dropdown(self, test_setup):
        self.bp.get_items_from_dropdown(AuthLocators.DAYS)

        for item in self.bp.items:
            self.bp.validate_item_is_selected(AuthLocators.DAYS, item)

    @allure.step("Each item from month dropdown can be selected")
    def test_month_dropdown(self, test_setup):
        self.bp.get_items_from_dropdown(AuthLocators.MONTHS)

        for item in self.bp.items:
            self.bp.validate_item_is_selected(AuthLocators.MONTHS, item)

    #
    @allure.step("Each item from year dropdown can be selected")
    def test_year_dropdown(self, test_setup):
        self.bp.get_items_from_dropdown(AuthLocators.YEARS)

        for item in self.bp.items:
            self.bp.validate_item_is_selected(AuthLocators.YEARS, item)

    @allure.step("Each item from state dropdown can be selected")
    def test_state_dropdown(self, test_setup):
        self.bp.get_items_from_dropdown(AuthLocators.STATE)

        for item in self.bp.items:
            self.bp.validate_item_is_selected(AuthLocators.STATE, item)
