#!/usr/local/bin python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.homePageLocators import HomePageLocators as hpl
import allure
import time

"""All items in home page header"""

class Header:

     def __init__(self, driver):
         self.driver = driver
         self.wait = WebDriverWait(self.driver.instance, 10)

         self.sign_in_xp = hpl.sign_in_xp

     @allure.step("Sign in button is clickable")
     def sign_in_button(self):
         self.sign_in_click = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.sign_in_xp)))
         assert self.sign_in_click.is_displayed()
         self.sign_in_click.click()


