from settings.webdriver import Driver
from page_objects.basePage import BasePage
from data.dataGenerators import *
from locators.authPageLocators import AuthLocators as al
from locators.homePageLocators import HomePageLocators as hpl
import pytest
import allure

"""Test to check if a new user can be created"""


class TestAuth():
    postal_value = str(random.randint(10000, 99999))
    mobile_value = str(random.randint(100000000, 999999999))
    state_value = str(random.randint(1, 50))
    days_value = str(random.randint(1, 31))
    month_value = str(random.randint(1, 12))
    years_value = str(random.randint(1900, 2019))

    sign_in = hpl.sign_in
    email_create = al.email_create
    submit_create = al.submit_create
    register = al.register
    customer_tab = al.customer_tab

    set_dict = {
        al.checkbox_gender_male: None,
        al.cust_fname: name_generator(),
        al.cust_lname: surname_generator(),
        al.password: password_generator(),
        al.days: days_value,
        al.months: month_value,
        al.years: years_value,
        al.newsletter: None,
        al.offers: None,
        al.state: state_value,
        al.city: "Washington",
        al.company: "Company",
        al.address: "White House Avenue",
        al.postal: postal_value,
        al.mobile: mobile_value
    }

    @pytest.fixture()
    def test_setup(self):
        self.driver = Driver()
        self.bp = BasePage(self.driver)
        yield
        self.bp.driver.instance.quit()

    @allure.step("New user can be created")
    def test_create_account(self, test_setup):
        self.driver.navigate('http://automationpractice.com/index.php')
        self.bp.click(self.sign_in)
        self.driver.instance.implicitly_wait(3)
        self.bp.set(self.email_create, mail_generator())
        self.bp.click(self.submit_create)

        for key, value in self.set_dict.items():
            self.bp.set(key, value)

        self.bp.click(self.register)
        self.bp.validate_element_present(self.customer_tab)
