from settings.webdriver import Driver
from page_objects.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class TestHomePageSlider():

    def setup(self):
        self.driver = Driver()
        self.bp = BasePage(self.driver)
        self.driver.navigate("http://automationpractice.com")

    # def test_home_page_slider(self):
    #     self.bp.validate_element_present(HomePageLocators.SLIDER_PIC_1)
    #     self.bp.validate_element_present(HomePageLocators.SLIDER_PIC_2)
    #     self.bp.validate_element_present(HomePageLocators.SLIDER_PIC_3)

    def test_home_page_slider_by_arrows(self):
        self.bp.validate_element_present(HomePageLocators.SLIDER_PIC_1)
        self.bp.click(HomePageLocators.NEXT_ARROW)
        self.bp.validate_element_present(HomePageLocators.SLIDER_PIC_2)
        self.bp.click(HomePageLocators.NEXT_ARROW, wait=2)
        self.bp.validate_element_present(HomePageLocators.SLIDER_PIC_3)

    def teardown(self):
        self.driver.teardown()

