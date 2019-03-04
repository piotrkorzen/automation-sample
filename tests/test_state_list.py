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
        yield
        self.driver.instance.quit()

    def test_state_lists(self, test_setup):
        create_account = CreateAccount(self.driver)
        dropdowns = CheckDropdownItemsForm(self.driver)

        self.driver.navigate(os.getenv('u'))
        sign_in = Header(self.driver)
        sign_in.sign_in_button()

        create_account.enter_email(mail_generator())

        dropdowns.check_days_dropdown()
        dropdowns.check_months_dropdown()
        dropdowns.check_years_dropdown()
        dropdowns.check_state_dropdown()

