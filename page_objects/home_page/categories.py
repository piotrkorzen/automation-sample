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

    @allure.step("Sort products by")
    def sort_by_all(self):
        self.get_items_from_dropdown(self.sort_by_list)

    def sort_by_price_highest_first(self):
        self.select(self.sort_by_list, "Price: Highest first")

    def validate_sort_products(self):
        item_list = []
        prices = self.driver.instance.find_elements_by_xpath("//div[@class='right-block']//span[@class='price product-price']")
        for item in prices:
            prices2 = item.text
            pr = prices2.strip("$")
            print(pr)
        # print(prices2)
        # soup = BeautifulSoup(plain_text,
        #                      features="html.parser")  # this format source code to more readable (sorting, searching things)
        # for link in soup.findAll('a', {
        #     'class': 'woocommerce-LoopProduct-link'}):  # this loop finds all links ('a') which class = woocommerce-loop-product__title
        #     href = link.get('href')
