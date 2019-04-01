from selenium.webdriver.common.by import By


class CheckboxLocators:

    # groups of checkboxes
    group_categories_xp         = (By.XPATH, "//input[contains(@id, 'layered_category')][@type='checkbox']")
    group_size_xp               = (By.XPATH, "//input[contains(@id, 'layered_id_attribute_group')][@type='checkbox']")
    group_color_xp              = (By.XPATH, "//ul[@id='ul_layered_id_attribute_group_3']//input[contains(@id, 'layered_id_attribute')][@type='button']")
    group_compositions_xp       = (By.XPATH, "//ul[@id='ul_layered_id_feature_5']//input[contains(@id, 'layered_id_feature')][@type='checkbox']")
    group_styles_xp             = (By.XPATH, "//ul[@id='ul_layered_id_feature_6']//input[contains(@id, 'layered_id_feature')][@type='checkbox']")
    group_properties_xp         = (By.XPATH, "//ul[@id='ul_layered_id_feature_7']//input[contains(@id, 'layered_id_feature')][@type='checkbox']")
    group_availability_xp       = (By.XPATH, "//ul[@id='ul_layered_quantity_0']//input[contains(@id, 'layered_quantity_1')][@type='checkbox']")
    group_manufacturer_xp       = (By.XPATH, "//ul[@id='ul_layered_manufacturer_0']//input[contains(@id, 'layered_manufacturer_1')][@type='checkbox']")
    group_condition_xp          = (By.XPATH, "//ul[@id='ul_layered_condition_0']//input[contains(@id, 'layered_condition_new')][@type='checkbox']")

    slider_xp                   = (By.XPATH, "//div[@class='layered_price']//a[1]")