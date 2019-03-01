from locators.authPageLocators import AuthLocators as apl
from page_objects.basePage import BasePage
import allure
import random
import time

"""All items connected with authorization e.g. create account, login into account"""

class CreateAccount(BasePage):

    email_create = apl.email_create_id
    submit_create = apl.submit_create_id

    @allure.step("Enter email and create account")
    def enter_email(self, email):
        self.send_keys(self.email_create, email)
        self.click(self.submit_create)

class FillAccountForm(BasePage):

    gender_man = apl.gender_male_css
    cust_fname = apl.cust_fname_id
    cust_lname = apl.cust_lname_id
    password = apl.password_id
    days = apl.days_id
    months = apl.months_id
    years = apl.years_id
    state = apl.state_id
    newsletter = apl.newsletter_id
    offers = apl.offers_id
    company = apl.company_id
    address = apl.address_id
    city = apl.city_id
    postal = apl.postal_id
    mobile = apl.mobile_id
    register = apl.register_xp
    days_value = random.randint(1, 31)
    month_value = random.randint(1, 12)
    years_value = random.randint(1900, 2019)
    state_value = random.randint(1, 50)
    postal_value = random.randint(10000, 99999)
    mobile_value = random.randint(100000000, 999999999)

    @allure.step("Fill all inputs - create account form")
    def fill_form_inputs(self, name, surname, password):
        self.send_keys(self.cust_fname, name)
        self.send_keys(self.cust_lname, surname)
        self.send_keys(self.password, password)
        self.send_keys(self.company, "Company")
        self.send_keys(self.city, "Washington")
        self.send_keys(self.address, "White House Avenue")
        self.send_keys(self.postal, self.postal_value)
        self.send_keys(self.mobile, self.mobile_value)

    @allure.step("Choose date of birth - create account form")
    def fill_form_date_of_birth(self):
        self.select(self.days, self.days_value)
        self.select(self.months, self.month_value)
        self.select(self.years, self.years_value)

    @allure.step("Choose state from lists - create account form")
    def fill_form_address(self):
        self.select(self.state, self.state_value)

    @allure.step("Mark checkboxes - create account form")
    def fill_form_checkboxes(self):
        self.click(self.gender_man)
        self.click(self.newsletter)
        self.click(self.offers)

    @allure.step("Click register - create account form")
    def click_register(self):
        self.click_clickable(self.register)