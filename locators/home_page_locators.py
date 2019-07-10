import os


class HomePageLocators:
    URL = os.getenv('URL')

    SIGN_IN = "//a[@title='Log in to your customer account']"

    """products on home page"""
    ALL_PRODUCTS = "//a[@class='product_img_link']"
    ADD_TO_CART = "//a[@title='Add to cart']"
    ICON_OK = "//i[@class='icon-ok']"
    CLOSE_PRODUCT_LAYER = "//span[@title='Close window']"
    CART_VIEW = "//a[@title='View my shopping cart']"
    RM_FROM_CART = "//a[@class='ajax_cart_block_remove_link']"
    EMPTY_CART_INFO = "//span[@class='ajax_cart_no_product']"
