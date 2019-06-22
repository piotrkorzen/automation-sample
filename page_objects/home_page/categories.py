from page_objects.basePage import BasePage
import allure


class Sort(BasePage):

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
            print(values, sort_asc, "Ascending sorting is valid")
            assert True
        else:
            print(values, sort_asc, "Ascending sorting is NOT valid")
            assert False

    @allure.step("Validate sort desc")
    def validate_sort_desc(self, values):
        sort_desc = sorted(values, reverse=True)
        if sort_desc == values:
            print(values, sort_desc, "Descending sorting is valid")
            assert True
        else:
            print(values, sort_desc, "Descending sorting is NOT valid")
            assert False
