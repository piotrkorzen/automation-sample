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

    def test_create_account(self, test_setup):
        self.driver.navigate(os.getenv('u'))
        sign_in = Header(self.driver)
        sign_in.sign_in_button()
        create_account = CreateAccount(self.driver)
        create_account.enter_email(mail_generator())
        fill_form = FillAccountForm(self.driver)
        fill_form.fill_form_checkboxes()
        fill_form.fill_form_inputs(name_generator(), surname_generator(), password_generator())
        fill_form.fill_form_date_of_birth()
        fill_form.fill_form_address()
        fill_form.click_register()
        time.sleep(10)

