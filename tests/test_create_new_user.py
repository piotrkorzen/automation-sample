from settings.webdriver import Driver
from page_objects.base_page import BasePage
from locators.auth_page_locators import AuthLocators
from locators.home_page_locators import HomePageLocators
from faker import Faker
import random
import pytest
import allure

"""Test to check if a new user can be created"""


class TestAuth():
    STATE_VALUE = str(random.randint(1, 50))
    MONTH_VALUE = str(random.randint(1, 12))
    DAYS_VALUE = str(random.randint(1, 31))
    YEARS_VALUE = str(random.randint(1900, 2019))
    FAKE = Faker()

    SET_DICT = {
        AuthLocators.CHECKBOX_GENDER_NAME: None,
        AuthLocators.CUST_FNAME: FAKE.first_name(),
        AuthLocators.CUST_LNAME: FAKE.last_name(),
        AuthLocators.PASSWORD: FAKE.sentence(nb_words=3),
        AuthLocators.MONTHS: MONTH_VALUE,
        AuthLocators.DAYS: DAYS_VALUE,
        AuthLocators.YEARS: YEARS_VALUE,
        AuthLocators.NEWSLETTER: None,
        AuthLocators.OFFERS: None,
        AuthLocators.STATE: STATE_VALUE,
        AuthLocators.CITY: FAKE.city(),
        AuthLocators.COMPANY: FAKE.company(),
        AuthLocators.ADDRESS: FAKE.street_name(),
        AuthLocators.POSTAL: FAKE.zipcode(),
        AuthLocators.MOBILE: FAKE.msisdn()
    }

    def setup(self):
        self.driver = Driver()
        self.bp = BasePage(self.driver)


    @allure.step("New user can be created")
    def test_create_account(self):
        self.driver.navigate("http://automationpractice.com/index.php")
        self.bp.click(HomePageLocators.SIGN_IN)
        self.bp.set(AuthLocators.EMAIL_CREATE, self.FAKE.email())
        self.bp.click(AuthLocators.SUBMIT_CREATE)
        self.bp.wait(AuthLocators.CHECKBOX_GENDER_NAME)

        for key, value in self.SET_DICT.items():
            self.bp.set(key, value)

        self.bp.click(AuthLocators.REGISTER)
        self.bp.validate_element_present(AuthLocators.CUSTOMER_TAB)

    def teardown(self):
        self.bp.driver.instance.quit()