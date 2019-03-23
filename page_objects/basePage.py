from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def get(self, url):
        self.driver.navigate(url)

    def click(self, locator):
        WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located(
            (locator))).click()

    def click_clickable(self, locator):
        WebDriverWait(self.driver.instance, 10).until(EC.element_to_be_clickable(
            (locator))).click()

    def send_keys(self, locator, value):
        WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located(
            (locator))).send_keys(value)

    def select(self, locator, value):
        self.driver.instance.implicitly_wait(2)
        self.option = Select(self.driver.instance.find_element(*locator))
        self.option.select_by_visible_text(str(value))

    def validate_element_present(self, locator):
        element = WebDriverWait(self.driver.instance, 25).until(EC.visibility_of_element_located(
            (locator)))
        assert element.is_displayed()

    def validate_element_not_present(self, locator):
        element = WebDriverWait(self.driver.instance, 10).until(EC.invisibility_of_element_located(
            (locator)))
        assert element == True

    def validate_url(self, url):
        WebDriverWait(self.driver.instance, 10).until(
            lambda driver: self.driver.instance.current_url == url)

    def switch_to_window(self, window):
        self.driver.instance.switch_to.window(self.driver.instance.window_handles[window])

    def execute_script(self, script):
        self.driver.instance.execute_script(script)

    def wait(self, locator):
        WebDriverWait(self.driver.instance, 15).until(EC.visibility_of_element_located(
            (locator)))

    def hover(self, locator):
        WebDriverWait(self.driver.instance, 10).until(
            lambda driver: self.driver.instance.find_element(*locator))
        element = self.driver.instance.find_element(*locator)
        hover = ActionChains(self.driver.instance).move_to_element(element)
        hover.perform()

    def get_items_from_dropdown(self, locator):
        self.items = []
        element = WebDriverWait(self.driver.instance, 10).until(
            lambda driver: self.driver.instance.find_element(*locator))
        all_options = element.find_elements_by_tag_name("option" or "mer-option")
        for option in all_options:
            self.item = option.get_attribute("text")
            self.items.append(self.item)
        self.items_counter = len(self.items)
        print(*self.items, sep='\n')
        print("The number of items on the list is: ", self.items_counter)

    # function for validate is element selected correctly
    def validate_item_is_selected(self, locator, value):
        self.select(locator, value)
        if self.option.first_selected_option.get_attribute('text') == value:
            assert True
        else:
            print("Item ", value, "has not been selected")
            raise AssertionError("Items have not been selected")
