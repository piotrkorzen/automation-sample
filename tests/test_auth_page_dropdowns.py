from settings.webdriver import Driver
import os
import pytest
from page_objects.home_page.header import Header
from page_objects.auth_page.authPage import *
from data.dataGenerators import *


class TestAuth():

    @pytest.fixture()
    def test_setup(self):
        self.driver = Driver()
        self.create_account = CreateAccount(self.driver)
        self.dropdowns = CheckDropdownItemsForm(self.driver)
        self.sign_in = Header(self.driver)
        self.driver.navigate("http://automationpractice.com")
        self.sign_in.sign_in_button()
        self.create_account.enter_email(mail_generator())
        yield
        self.driver.instance.quit()

    def test_days_list(self, test_setup):
        self.dropdowns.check_days_dropdown()

    def test_month_list(self, test_setup):
        self.dropdowns.check_months_dropdown()

    def test_year_list(self, test_setup):
        self.dropdowns.check_years_dropdown()

    def test_state_list(self, test_setup):
        self.dropdowns.check_state_dropdown()