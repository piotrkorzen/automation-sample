from settings.webdriver import Driver
import os
import pytest
from page_objects.home_page.categories import WomenCategories

class TestWomenCategories():


    @pytest.fixture()
    def test_setup(self):
        self.driver = Driver()
        yield
        self.driver.instance.quit()

    """Test for check visibility of subcategories from home page"""

    def test_subcategories_are_visible(self, test_setup):
        self.driver.navigate(os.getenv('u'))

        wm = WomenCategories(self.driver)

        wm.women_cat_hover()
        wm.women_subcategories_tops_present()
        wm.women_subcategories_dresses_present()



