from page_objects.basePage import BasePage
from locators.checkboxLocators import CheckboxLocators as chl

import time



class Checboxes(BasePage):

    group_size = chl.group_size_xp
    compositions = chl.group_compositions_xp
    styles = chl.group_styles_xp
    properties = chl.group_properties_xp
    availability = chl.group_availability_xp
    manufacturer = chl.group_manufacturer_xp
    condition = chl.group_condition_xp
    slider1 = chl.slider_xp
    tops=size_s=cotton=casual=colorful_dress=\
        in_stock=fashion_man=new=2

    def click_all_checkboxes(self, locator, check=None):
        checkboxes = self.driver.instance.find_elements(*locator)

        if check is not None:
            checkboxes[check].click()
        elif check == None:
            for checkbox in checkboxes:
                if not checkbox.is_selected():
                    checkbox.click()
                if checkbox.is_selected():
                    assert True
                else:
                    assert False
        else:
            print("Any checkbox haven't been selected!")

    def price_slider(self):
        self.slider(self.slider1, 40,0)


    def click_size_checkboxes(self):
        self.click_all_checkboxes(self.group_size, self.size_s)

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
