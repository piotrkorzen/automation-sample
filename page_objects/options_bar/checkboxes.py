from page_objects.basePage import BasePage
from locators.checkboxLocators import CheckboxLocators as chl

import time



class Checboxes(BasePage):

    group_size = chl.group_size_xp
    compositions = chl.group_compositions_xp

    def click_size_checkboxes(self):
        self.click_all_checkboxes(self.group_size)

    def click_composition_checkboxes(self):
        self.click_all_checkboxes(self.compositions)

        # for i in range(3):
        #     time.sleep(3)
        #     self.driver.instance.find_element_by_xpath(
        #         "//a[contains(@href, 'http://automationpractice.com/index.php?id_category=3&controller=category#size')]").click()
