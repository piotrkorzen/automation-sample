from locators.homePageLocators import HomePageLocators as hpl
from page_objects.basePage import BasePage
import allure


class WomenCategories(BasePage):

    women_cat = hpl.women_cat_xp
    tshirt_sub = hpl.tshirts_sub_xp
    blouses_sub = hpl.blouses_sub_xp
    casual_d_sub = hpl.casual_d_sub_xp
    evening_d_sub = hpl.evening_d_sub_xp
    summer_d_sub = hpl.summer_d_sub_xp_
    dresses_cat = hpl.dresses_cat_xp

    @allure.step("Hover on 'Women' category")
    def women_cat_hover(self):
        self.hover(self.women_cat)

    @allure.step("Hover on 'Dresses' category")
    def dresses_cat_hover(self):
        self.hover(self.dresses_cat)

    @allure.step("Validate women Tops subcategories present")
    def women_subcategories_tops_present(self):
        self.validate_element_present(self.tshirt_sub)
        self.validate_element_present(self.blouses_sub)

    @allure.step("Validate women Dresses subcategories present")
    def women_subcategories_dresses_present(self):
        self.validate_element_present(self.casual_d_sub)
        self.validate_element_present(self.evening_d_sub)
        self.validate_element_present(self.summer_d_sub)
