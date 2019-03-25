from page_objects.basePage import BasePage
from locators.checkboxLocators import CheckboxLocators as chl

import time



class Checboxes(BasePage):

    group_size = chl.group_size_xp
    compositions = chl.group_compositions_xp
    styles = chl.styles_xp
    properties = chl.properties_xp
    availability = chl.availability_xp
    manufacturer = chl.manufacturer_xp
    condition = chl.condition_xp

    def click_all_checkboxes(self, locator):
        checkboxes = self.driver.instance.find_elements(*locator)
        for checkbox in checkboxes:
            if not checkbox.is_selected():
                checkbox.click()
            if checkbox.is_selected():
                assert True
            else:
                assert False

    def click_size_checkboxes(self):
        self.click_all_checkboxes(self.group_size)

    def click_composition_checkboxes(self):
        self.click_all_checkboxes(self.compositions)

    def click_style_checkboxes(self):
        self.click_all_checkboxes(self.styles)

    def click_properties_checkboxes(self):
        self.click_all_checkboxes(self.properties)

    def click_availability_checkbox(self):
        self.click_all_checkboxes(self.availability)

    def click_manufacturer_checkbox(self):
        self.click_all_checkboxes(self.manufacturer)

    def click_condition_checkbox(self):
        self.click_all_checkboxes(self.condition)

        # for i in range(3):
        #     time.sleep(3)
        #     self.driver.instance.find_element_by_xpath(
        #         "//a[contains(@href, 'http://automationpractice.com/index.php?id_category=3&controller=category#size')]").click()
