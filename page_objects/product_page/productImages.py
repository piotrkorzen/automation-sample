from page_objects.basePage import BasePage
from locators.productPageLocators import ProductPageLocators as ppl

class ProductImages(BasePage):

    image_lst = ppl.image_lst_xp
    close_image = ppl.close_product_image_xp
    image_layer = ppl.image_layer_xp
    image_box = ppl.image_box_xp

    def show_all_images(self):
        images = self.driver.instance.find_elements_by_xpath(self.image_lst)

        for image in images:
            image.click()
            self.validate_element_present(self.image_box)
            self.click_clickable(self.close_image)
            self.validate_element_not_present(self.image_layer)