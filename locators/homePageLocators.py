import os
from selenium.webdriver.common.by import By

class HomePageLocators:

    url = os.getenv('u')
    sign_in_xp = (By.XPATH, "//a[@title='Log in to your customer account']")
