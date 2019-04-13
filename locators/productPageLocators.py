from selenium.webdriver.common.by import By

class ProductPageLocators:
    add_to_cart_xp              = (By.XPATH, "//span[contains(text(),'Add to cart')]")
    layer_cart_xp               = (By.XPATH, "//div[@id='layer_cart']//div[@class='clearfix']")
    close_layer_cart_xp         = (By.XPATH, "//span[@title='Close window']")
    shopping_cart_xp            = (By.XPATH, "//a[@title='View my shopping cart']")
    remove_product_from_cart_xp = (By.XPATH, "//a[@class='ajax_cart_block_remove_link']")
    cart_info_xp                = (By.XPATH, "//div[@class='cart-info']")