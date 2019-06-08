from selenium.webdriver.common.by import By

class ProductPageLocators:
    add_to_cart_xp              = (By.XPATH, "//span[contains(text(),'Add to cart')]")
    layer_cart_xp               = (By.XPATH, "//div[@id='layer_cart']//div[@class='clearfix']")
    close_layer_cart_xp         = (By.XPATH, "//span[@title='Close window']")
    shopping_cart_xp            = (By.XPATH, "//a[@title='View my shopping cart']")
    remove_product_from_cart_xp = (By.XPATH, "//a[@class='ajax_cart_block_remove_link']")
    cart_info_xp                = (By.XPATH, "//div[@class='cart-info']")
    image_lst_xp                = "//img[contains(@id,'thumb_')]"
    close_product_image_xp      = (By.XPATH, "//a[@class='fancybox-item fancybox-close']")
    image_layer_xp              = (By.XPATH, "//div[@class='fancybox-overlay fancybox-overlay-fixed']")
    image_box_xp                = (By.XPATH, "//img[@class='fancybox-image']")

    """Product page items"""
    main_image_box_xp           = (By.XPATH, "//img[@itemprop='image']")
    name_xp                     = (By.XPATH, "//h1[@itemprop='name']")
    description_xp              = (By.XPATH, "//div[@id='short_description_content']")
    social_media_xp             = (By.XPATH, "//p[@class='socialsharing_product list-inline no-print']")
    send_to_friend_button_xp    = (By.XPATH, "//a[@id='send_friend_button']")
    print_button_xp             = (By.XPATH, "//li[@class='print']")
    views_block_xp              = (By.XPATH, "//div[@id='views_block']")
    box_info_product_xp         = (By.XPATH, "//div[@class='box-info-product']")

