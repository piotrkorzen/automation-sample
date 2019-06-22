from settings.webdriver import Driver
from page_objects.basePage import BasePage
from locators.homePageLocators import HomePageLocators as hpl
from locators.authPageLocators import AuthLocators as al
from data.dataGenerators import *
import pytest
import allure

"""Test to check whether each item in dropdown list can be selected"""


class TestAuth():
    sign_in = hpl.sign_in
    email_create = al.email_create
    submit_create = al.submit_create
    days = al.days
    months = al.months
    years = al.years
    state = al.state

    @pytest.fixture()
    def test_setup(self):
        self.driver = Driver()
        self.bp = BasePage(self.driver)
        self.driver.navigate('http://automationpractice.com/index.php')
        self.bp.click(self.sign_in)
        self.driver.instance.implicitly_wait(3)
        self.bp.set(self.email_create, mail_generator())
        self.bp.click(self.submit_create)
        yield
        self.driver.instance.quit()

    @allure.step("Each item from days dropdown can be selected")
    def test_days_dropdown(self, test_setup):
        self.bp.get_items_from_dropdown(self.days)

        for item in self.bp.items:
            self.bp.validate_item_is_selected(self.days, item)

    @allure.step("Each item from month dropdown can be selected")
    def test_month_dropdown(self, test_setup):
        self.bp.get_items_from_dropdown(self.months)

        for item in self.bp.items:
            self.bp.validate_item_is_selected(self.months, item)

    @allure.step("Each item from year dropdown can be selected")
    def test_year_dropdown(self, test_setup):
        self.bp.get_items_from_dropdown(self.years)

        for item in self.bp.items:
            self.bp.validate_item_is_selected(self.years, item)

    @allure.step("Each item from state dropdown can be selected")
    def test_state_dropdown(self, test_setup):
        self.bp.get_items_from_dropdown(self.state)

        for item in self.bp.items:
            self.bp.validate_item_is_selected(self.state, item)
