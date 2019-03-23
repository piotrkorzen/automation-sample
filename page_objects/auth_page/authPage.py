from locators.authPageLocators import AuthLocators as apl
from page_objects.basePage import BasePage
import allure
import random

"""Class contains functions for register new user"""


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
    dropdown_state_label = apl.dropdown_state_label_xp

    @allure.step("Fill basic - create account form")
    def fill_form_basics(self, name, surname, password):
        self.send_keys(self.cust_fname, name)
        self.send_keys(self.cust_lname, surname)
        self.send_keys(self.password, password)

    @allure.step("Fill address - create account form")
    def fill_form_address(self, postal, mobile):
        self.send_keys(self.company, "Company")
        self.send_keys(self.city, "Washington")
        self.send_keys(self.address, "White House Avenue")
        self.send_keys(self.postal, postal)
        self.send_keys(self.mobile, mobile)

    @allure.step("Choose date of birth - create account form")
    def fill_form_date_of_birth(self):
        self.select(self.days, self.days_value)
        self.select(self.months, self.month_value)
        self.select(self.years, self.years_value)

    @allure.step("Choose state from lists - create account form")
    def fill_form_state(self, state):
        self.select(self.state, state)

    @allure.step("Mark checkboxes - create account form")
    def fill_form_checkboxes(self):
        self.click_clickable(self.gender_man)
        self.click_clickable(self.newsletter)
        self.click_clickable(self.offers)

    @allure.step("Click register - create account form")
    def click_register(self):
        self.click_clickable(self.register)


"""Class contains functions for checking is each item can be selected from form dropdown lists"""


class CheckDropdownItemsForm(FillAccountForm):

    @allure.step("Each item from days dropdown can be selected")
    def check_days_dropdown(self):
        self.get_items_from_dropdown(self.days)

        for item in self.items:
            self.validate_item_is_selected(self.days, item)

    @allure.step("Each item from months dropdown can be selected")
    def check_months_dropdown(self):
        self.get_items_from_dropdown(self.months)

        for item in self.items:
            self.validate_item_is_selected(self.months, item)

    @allure.step("Each item from years dropdown can be selected")
    def check_years_dropdown(self):
        self.get_items_from_dropdown(self.years)

        for item in self.items:
            self.validate_item_is_selected(self.years, item)

    @allure.step("Each item from state dropdown can be selected")
    def check_state_dropdown(self):
        self.get_items_from_dropdown(self.dropdown_state_label)

        for item in self.items:
            self.validate_item_is_selected(self.state, item)
