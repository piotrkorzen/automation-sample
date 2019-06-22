import os


class HomePageLocators:
    url                 = os.getenv('u')

    sign_in             = "//a[@title='Log in to your customer account']"

    # products on home page
    all_products        = "//a[@class='product_img_link']"
    add_to_cart         = "//a[@title='Add to cart']"
    icon_ok             = "//i[@class='icon-ok']"
    close_product_layer = "//span[@title='Close window']"
    cart_view           = "//a[@title='View my shopping cart']"
    rm_from_cart        = "//a[@class='ajax_cart_block_remove_link']"
    empty_cart_info     = "//span[@class='ajax_cart_no_product']"
