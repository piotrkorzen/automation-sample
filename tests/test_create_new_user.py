from settings.webdriver import Driver
import os
import pytest
from page_objects.home_page.header import Header
from page_objects.auth_page.authPage import *
from data.dataGenerators import *
import random


class TestAuth():

    postal_value = random.randint(10000, 99999)
    mobile_value = random.randint(100000000, 999999999)
    state_value = random.randint(1, 50)

    @pytest.fixture()
    def test_setup(self):
        self.driver = Driver()
        yield
        self.driver.instance.quit()

    def test_create_account(self, test_setup):
        self.driver.navigate(os.getenv('u'))
        sign_in = Header(self.driver)
        sign_in.sign_in_button()

        create_account = CreateAccount(self.driver)
        create_account.enter_email(mail_generator())

        fill_form = FillAccountForm(self.driver)
        self.driver.instance.implicitly_wait(3)
        fill_form.fill_form_checkboxes()
        fill_form.fill_form_basics(name_generator(), surname_generator(), password_generator())
        fill_form.fill_form_address(self.postal_value, self.mobile_value)
        fill_form.fill_form_date_of_birth()
        fill_form.fill_form_state(self.state_value)
        fill_form.click_register()
