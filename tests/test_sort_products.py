from settings.webdriver import Driver
from locators.categories_locators import CategoriesLocators
from page_objects.home_page.categories import Sort


class TestSortProducts():

    def setup(self):
        self.driver = Driver()
        self.s = Sort(self.driver)
        self.driver.navigate("http://automationpractice.com/index.php?id_category=3&controller=category")

    def test_sort_by_price_asc(self):
        self.s.set(CategoriesLocators.SORT_SELECT, "Price: Lowest first")
        self.s.validate_sort_asc(self.s.get_product_price(CategoriesLocators.PRICES))

    def test_sort_by_price_desc(self):
        self.s.set(CategoriesLocators.SORT_SELECT, "Price: Highest first")
        self.s.validate_sort_desc(self.s.get_product_price(CategoriesLocators.PRICES))

    def test_sort_by_a_z(self):
        self.s.set(CategoriesLocators.SORT_SELECT, "Product Name: A to Z")
        self.s.validate_sort_asc(self.s.get_product_names(CategoriesLocators.PRODUCTS_NAME))

    def test_sort_by_z_a(self):
        self.s.set(CategoriesLocators.SORT_SELECT, "Product Name: Z to A")
        self.s.validate_sort_desc(self.s.get_product_names(CategoriesLocators.PRODUCTS_NAME))

    def teardown(self):
        self.driver.instance.quit()
