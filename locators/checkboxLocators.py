from selenium.webdriver.common.by import By


class CheckboxLocators:

    group_size_xp         = (By.XPATH, "//input[contains(@id, 'layered_id_attribute_group')][@type='checkbox']")
    group_compositions_xp = (By.XPATH, "//input[contains(@id, 'layered_id_feature')][@type='checkbox']")