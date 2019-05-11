from selenium.webdriver.common.by import By


class CategoriesLocators:

    sort_by_list_xp = (By.XPATH, "//select[@id='selectProductSort']")
    prices_xp       = ("//div[@class='right-block']//span[@class='price product-price']")
    products_xp     = ("//div[@id='center_column']//a[@class='product-name']")
