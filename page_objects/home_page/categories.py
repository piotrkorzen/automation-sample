import allure
import logging
from page_objects.base_page import BasePage


class Sort(BasePage):
    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s:%(message)s")

    @allure.step("Get product price")
    def get_product_price(self, value):
        self.price_list = []
        prices = self.driver.instance.find_elements_by_xpath(value)
        for item in prices:
            dollar_price = item.text
            price = dollar_price.strip("$")
            self.price_list.append(price)
        return self.price_list

    @allure.step("Get product names")
    def get_product_names(self, value):
        self.product_list = []
        products = self.driver.instance.find_elements_by_xpath(value)
        for item in products:
            product_name = item.text
            self.product_list.append(product_name)
        return self.product_list

    @allure.step("Validate sort asc")
    def validate_sort_asc(self, values):
        sort_asc = sorted(values)
        if sort_asc == values:
            logging.info("{}\n{} - Ascending sorting is valid".format(values, sort_asc))
            assert True
        else:
            logging.error("{}\n{} - Ascending sorting is NOT valid".format(values, sort_asc))
            assert False

    @allure.step("Validate sort desc")
    def validate_sort_desc(self, values):
        sort_desc = sorted(values, reverse=True)
        if sort_desc == values:
            logging.info("{}\n{} - Descending sorting is valid".format(values, sort_desc))
            assert True
        else:
            logging.error("{}\n{} - Descending sorting is NOT valid".format(values, sort_desc))
            assert False
