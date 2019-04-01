from page_objects.basePage import BasePage
from locators.checkboxLocators import CheckboxLocators as chl


class Checboxes(BasePage):
    categories = chl.group_categories_xp
    size = chl.group_size_xp
    color = chl.group_color_xp
    compositions = chl.group_compositions_xp
    styles = chl.group_styles_xp
    properties = chl.group_properties_xp
    availability = chl.group_availability_xp
    manufacturer = chl.group_manufacturer_xp
    condition = chl.group_condition_xp
    slider1 = chl.slider_xp

    def click_checkboxes(self, locator):
        checkboxes = self.driver.instance.find_elements(*locator)
        for checkbox in checkboxes:
            if not checkbox.is_selected():
                checkbox.click()
            if checkbox.is_selected():
                assert True
            else:
                assert False

    def price_slider(self):
        self.slider(self.slider1, 40, 0)

    def click_categories_checkboxes(self):
        self.click_checkboxes(self.categories)

    def click_size_checkboxes(self):
        self.click_checkboxes(self.size)

    def click_color_checkboxes(self):
        self.click_checkboxes(self.color)

    def click_composition_checkboxes(self):
        self.click_checkboxes(self.compositions)

    def click_style_checkboxes(self):
        self.click_checkboxes(self.styles)

    def click_properties_checkboxes(self):
        self.click_checkboxes(self.properties)

    def click_availability_checkbox(self):
        self.click_checkboxes(self.availability)

    def click_manufacturer_checkbox(self):
        self.click_checkboxes(self.manufacturer)

    def click_condition_checkbox(self):
        self.click_checkboxes(self.condition)