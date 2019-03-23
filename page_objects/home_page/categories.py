from locators.homePageLocators import HomePageLocators as hpl
from locators.categoriesLocators import CategoriesLocators as cl
from page_objects.basePage import BasePage
import allure
from bs4 import BeautifulSoup


class WomenCategories(BasePage):

    women_cat = hpl.women_cat_xp
    tshirt_sub = hpl.tshirts_sub_xp
    blouses_sub = hpl.blouses_sub_xp
    casual_d_sub = hpl.casual_d_sub_xp
    evening_d_sub = hpl.evening_d_sub_xp
    summer_d_sub = hpl.summer_d_sub_xp_

    @allure.step("Hover on 'Women' category")
    def women_cat_hover(self):
        self.hover(self.women_cat)

    @allure.step("Validate women Tops subcategories present")
    def women_subcategories_tops_present(self):
        self.validate_element_present(self.tshirt_sub)
        self.validate_element_present(self.blouses_sub)

    @allure.step("Validate women Dresses subcategories present")
    def women_subcategories_dresses_present(self):
        self.validate_element_present(self.casual_d_sub)
        self.validate_element_present(self.evening_d_sub)
        self.validate_element_present(self.summer_d_sub)

    @allure.step("Women category is clickable")
    def women_category_click(self):
        self.click_clickable(self.women_cat)

    @allure.step("T-shirts sub-category is clickable")
    def t_shirts_sub_click(self):
        self.click_clickable(self.tshirt_sub)

    @allure.step("Bloues sub-category is clickable")
    def blouses_sub_click(self):
        self.click_clickable(self.blouses_sub)

    @allure.step("Casual dresses sub-category is clickable")
    def casual_sub_click(self):
        self.click_clickable(self.casual_d_sub)

    @allure.step("Evening dresses sub-category is clickable")
    def evening_sub_click(self):
        self.click_clickable(self.evening_d_sub)

    @allure.step("Summer dresses sub-category is clickable")
    def summer_sub_click(self):
        self.click_clickable(self.summer_d_sub)

class WomenCategoriesProducts(WomenCategories):

    sort_by_list = cl.sort_by_list_xp
    prices = cl.prices_xp

    @allure.step("Sort products by")
    def sort_by_all(self):
        self.get_items_from_dropdown(self.sort_by_list)

    def sort_by_price_highest_first(self):
        self.select(self.sort_by_list, "Price: Highest first")

    def get_product_price(self):
        self.price_list = []
        prices = self.driver.instance.find_elements_by_xpath(self.prices)
        for item in prices:
            dollar_price = item.text
            price = dollar_price.strip("$")
            self.price_list.append(price)
        return self.price_list

    def validate_sort_prices_asc(self):
        sort_asc = sorted(self.get_product_price())
        if sort_asc == self.get_product_price():
            print(self.price_list, sort_asc, "Ascending sorting is valid")
            assert True
        else:
            print(self.price_list, sort_asc, "Ascending sorting is NOT valid")
            assert False

    def validate_sort_prices_desc(self):
        sort_desc = sorted(self.get_product_price(), reverse=True)
        if sort_desc == self.get_product_price():
            print(self.price_list, sort_desc, "Descending sorting is valid")
            assert True
        else:
            print(self.price_list, sort_desc, "Descending sorting is NOT valid")
            assert False
