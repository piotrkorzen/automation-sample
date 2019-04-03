from selenium.webdriver.common.by import By

class ProductPageLocators:
    add_to_cart_xp = (By.XPATH, "//span[contains(text(),'Add to cart')]")
    layer_cart_xp = (By.XPATH, "//div[@id='layer_cart']")