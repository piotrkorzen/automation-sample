import os
from selenium.webdriver.common.by import By


class HomePageLocators:

    url = os.getenv('u')

    sign_in_xp = (By.XPATH, "//a[@title='Log in to your customer account']")

    # products on home page

    product_xp = (By.XPATH, "//li[@class='ajax_block_product col-xs-12 col-sm-4 col-md-3 first-in-line first-item-of"
                            "-tablet-line first-item-of-mobile-line hovered']//img[@title='Faded Short Sleeve T-shirts']")

    product2_xp = (By.XPATH,
                   "//li[@class='ajax_block_product col-xs-12 col-sm-4 col-md-3 last-item-of-mobile-line hovered']//img[@title='Blouse']")

    product3_xp = (By.XPATH,
                   "//li[@class='ajax_block_product col-xs-12 col-sm-4 col-md-3 last-item-of-tablet-line first-item-of-mobile-line hovered']//img[@title='Printed Dress']")

    product4_xp = (By.XPATH,
                   "//li[@class='ajax_block_product col-xs-12 col-sm-4 col-md-3 last-in-line first-item-of-tablet-line last-item-of-mobile-line hovered']//img[@title='Printed Dress']")

    product5_xp = (By.XPATH,
                   "//li[@class='ajax_block_product col-xs-12 col-sm-4 col-md-3 first-in-line last-line first-item-of-mobile-line hovered']//img[@title='Printed Summer Dress']")

    product6_xp = (By.XPATH,
                   "//li[@class='ajax_block_product col-xs-12 col-sm-4 col-md-3 last-line last-item-of-tablet-line last-item-of-mobile-line hovered']//img[@title='Printed Summer Dress']")

    product7_xp = (By.XPATH, "//li[@class='ajax_block_product col-xs-12 col-sm-4 col-md-3 last-line first-item-of-"
                             "tablet-line first-item-of-mobile-line last-mobile-line hovered']//img[@title='Printed Chiffon Dress']")

    # categories and sub-categories

    women_cat_xp = (By.XPATH, "//a[@title='Women']")
    dresses_cat_xp = (By.XPATH, "//li[@class='sfHover']//a[@title='Dresses'][contains(text(),'Dresses')]']")
    tshirts_sub_xp = (By.XPATH, "//a[@title='T-shirts']")
    blouses_sub_xp = (By.XPATH, "//a[@title='Blouses']")
    casual_d_sub_xp = (By.XPATH, "//a[@title='Casual Dresses']")
    evening_d_sub_xp = (By.XPATH, "//a[@title='Evening Dresses']")
    summer_d_sub_xp_ = (By.XPATH, "//a[@title='Summer Dresses']")
