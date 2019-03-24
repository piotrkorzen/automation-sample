from page_objects.basePage import BasePage


class Checboxes(BasePage):

    def get_all_checkboxes(self):
        checkboxes = self.driver.instance.find_elements_by_xpath("//a[contains(@href, 'http://automationpractice.com/index.php?id_category=3&controller=category#size')]")
        for item in checkboxes:
            item_name = item.text
            self.click(item)
            print(item_name)
