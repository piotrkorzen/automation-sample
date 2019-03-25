from selenium.webdriver.common.by import By


class CheckboxLocators:

    group_size_xp         = (By.XPATH, "//input[contains(@id, 'layered_id_attribute_group')][@type='checkbox']")
    group_compositions_xp = (By.XPATH, "//ul[@id='ul_layered_id_feature_5']//input[contains(@id, 'layered_id_feature')][@type='checkbox']")
    styles_xp             = (By.XPATH, "//ul[@id='ul_layered_id_feature_6']//input[contains(@id, 'layered_id_feature')][@type='checkbox']")
    properties_xp         = (By.XPATH, "//ul[@id='ul_layered_id_feature_7']//input[contains(@id, 'layered_id_feature')][@type='checkbox']")
    availability_xp       = (By.XPATH, "//ul[@id='ul_layered_quantity_0']//input[contains(@id, 'layered_quantity_1')][@type='checkbox']")
    manufacturer_xp       = (By.XPATH, "//ul[@id='ul_layered_manufacturer_0']//input[contains(@id, 'layered_manufacturer_1')][@type='checkbox']")
    condition_xp          = (By.XPATH, "//ul[@id='ul_layered_condition_0']//input[contains(@id, 'layered_condition_new')][@type='checkbox']")