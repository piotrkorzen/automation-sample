from settings.webdriver import Driver
from page_objects.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.auth_page_locators import AuthLocators
from faker import Faker
import pytest
import allure
from datetime import datetime
from allure_commons.types import AttachmentType

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
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        allure.attach(self.driver.instance.get_screenshot_as_png(name="{}".format(now),
                      attachment_type=AttachmentType.PNG))

        self.driver.instance.quit()

    # def test_days_dropdown(self, test_setup):
    #     self.bp.get_items_from_dropdown(AuthLocators.DAYS)
    #
    #     for item in self.bp.items:
    #         self.bp.validate_item_is_selected(AuthLocators.DAYS, item)

    def test_month_dropdown(self, test_setup):
        self.bp.get_items_from_dropdown(AuthLocators.MONTHS)

        for item in self.bp.items:
            self.bp.validate_item_is_selected(AuthLocators.MONTHS, item)

    # def test_year_dropdown(self, test_setup):
    #     self.bp.get_items_from_dropdown(AuthLocators.YEARS)
    #
    #     for item in self.bp.items:
    #         self.bp.validate_item_is_selected(AuthLocators.YEARS, item)
    #
    # def test_state_dropdown(self, test_setup):
    #     self.bp.get_items_from_dropdown(AuthLocators.STATE)
    #
    #     for item in self.bp.items:
    #         self.bp.validate_item_is_selected(AuthLocators.STATE, item)
