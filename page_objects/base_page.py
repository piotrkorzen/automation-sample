from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, \
    ElementClickInterceptedException, InvalidElementStateException
from selenium.webdriver.support import expected_conditions as EC
import allure
import logging


class BasePage(object):
    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s:%(message)s")

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def locator(value):
        if value.startswith("//" or "/"):
            return By.XPATH, value
        elif value.startswith("#"):
            return By.CSS_SELECTOR, value
        else:
            return By.ID, value

    @allure.step("Getting the " + str({1}) + " has been successful")
    def get(self, url):
        return self.driver.navigate(url)

    @allure.step("The element " + str({1}) + " has been clicked")
    def click(self, value, wait=15):
        """function for click on single element"""
        try:
            return WebDriverWait(self.driver.instance, wait).until(EC.element_to_be_clickable(
                (self.locator(value)))).click()
        except ElementClickInterceptedException:
            return WebDriverWait(self.driver.instance, wait).until(EC.visibility_of_element_located(
                (self.locator(value)))).click()

    @allure.step("The element " + str({1}) + " with position " + str({2}) + " has been clicked")
    def click_element(self, value, element_number=0):
        """function for click on element from list of elements where we can choose which element is interesting for us
           e.g. we can choose particular product from product scope or iterate through all products"""
        self.elements_list = []
        elements = WebDriverWait(self.driver.instance, 10).until(
            lambda driver: self.driver.instance.find_elements(*self.locator(value)))
        for element in elements:
            self.elements_list.append(element)
        self.elements_list[element_number].click()

    @allure.step("The element " + str({1}) + " has been set")
    def set(self, value, send_value):
        """function for setting input values, checkboxes, radio buttons and dropdown lists"""
        inputs = ["input", "textarea"]
        if any(mark in value for mark in inputs):
            # for plain text areas"""
            if send_value is not None:
                condition = EC.visibility_of_element_located(self.locator(value))
                element = WebDriverWait(self.driver.instance, timeout=10).until(condition)
                element.clear(), element.send_keys(send_value)
            else:
                # for not hidden inputs in case of checkboxes and radio buttons
                try:
                    self.checkbox = self.driver.instance.find_element(*self.locator(value))
                    if not self.checkbox.is_selected():
                        self.checkbox.click()
                    if self.checkbox.is_selected():
                        assert True
                    else:
                        assert False
                # for hidden inputs in case of checkboxes and radio buttons
                except ElementNotVisibleException:
                    self.driver.instance.execute_script("arguments[0].click();", self.checkbox)
                except InvalidElementStateException:
                    self.driver.instance.execute_script("arguments[0].click();", self.checkbox)
        # for dropdown lists
        if "select" in value:
            self.option = Select(self.driver.instance.find_element(*self.locator(value)))
            try:
                self.option.select_by_visible_text(send_value)
            except NoSuchElementException:
                try:
                    self.option.select_by_value(send_value)
                except NoSuchElementException:
                    self.option.select_by_index(send_value)

    @allure.step("The element " + str({1}) + " has been presented")
    def validate_element_present(self, value):
        condition = EC.visibility_of_element_located(self.locator(value))
        element = WebDriverWait(self.driver.instance, timeout=20).until(condition)
        assert element.is_displayed()

    @allure.step("The element " + str({1}) + " has been NOT presented")
    def validate_element_not_present(self, value):
        condition = EC.invisibility_of_element_located(self.locator(value))
        element = WebDriverWait(self.driver.instance, timeout=10).until(condition)
        assert element == True

    @allure.step("Current url is equal to expected" + str({1}))
    def validate_url(self, url):
        WebDriverWait(self.driver.instance, 10).until(
            lambda driver: self.driver.instance.current_url == url)

    @allure.step("Switched to window" + str({1}) + " has been successful")
    def switch_to_window(self, window):
        self.driver.instance.switch_to.window(self.driver.instance.window_handles[window])

    @allure.step("Script " + str({1}) + " has been executed")
    def execute_script(self, *script):
        self.driver.instance.execute_script(script)

    def wait(self, value):
        WebDriverWait(self.driver.instance, timeout=10).until(EC.visibility_of_element_located(
            (self.locator(value))))

    @allure.step("Mouse is on " + str({1}) + " and element" + str({2}))
    def hover(self, value, element=0):
        self.all_elements = []
        products = WebDriverWait(self.driver.instance, timeout=10).until(
            lambda driver: self.driver.instance.find_elements(*self.locator(value)))
        for product in products:
            self.all_elements.append(product)
        hover = ActionChains(self.driver.instance).move_to_element(self.all_elements[element])
        hover.perform()

    @allure.step("The elements from " + str({1}) + " has been taken")
    def get_items_from_dropdown(self, value):
        """function returning items from dropdowns lists"""
        self.items = []
        element = WebDriverWait(self.driver.instance, 10).until(
            lambda driver: self.driver.instance.find_element(*self.locator(value)))
        all_options = element.find_elements_by_tag_name("option")
        for option in all_options:
            self.item = option.get_attribute("text")
            self.items.append(self.item)
        del self.items[0]
        self.items_counter = len(self.items)
        logging.info("Items:\n{}".format("\n".join(map(str, self.items))))
        logging.info("The number of items on the list is: {}".format(self.items_counter))
        return self.items

    @allure.step("The item " + str({2}) + " has been selected")
    def validate_item_is_selected(self, value, send_value):
        """function for validate element from dropdown list is selected correctly"""
        self.set(value, send_value)
        if self.option.first_selected_option.get_attribute('text') == send_value:
            assert True
        else:
            logging.error("Item {} has not been selected".format(value))
            raise AssertionError("Items have not been selected")

    @allure.step("The slider " + str({1}) + " is on a position")
    def slider(self, value, *offset):
        slider = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located(
            (self.locator(value))))
        move = ActionChains(self.driver.instance)
        move.click_and_hold(slider).move_by_offset(*offset).release().perform()
