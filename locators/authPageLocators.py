from selenium.webdriver.common.by import By


class AuthLocators:

    email_create_id         = (By.ID, "email_create")
    submit_create_id        = (By.ID, "SubmitCreate")
    gender_male_css         = (By.CSS_SELECTOR, "#id_gender1")
    cust_fname_id           = (By.ID, "customer_firstname")
    cust_lname_id           = (By.ID, "customer_lastname")
    password_id             = (By.ID, "passwd")
    days_id                 = (By.ID, "days")
    months_id               = (By.ID, "months")
    years_id                = (By.ID, "years")
    state_id                = (By.ID, "id_state")
    newsletter_id           = (By.ID, "newsletter")
    offers_id               = (By.ID, "optin")
    city_id                 = (By.ID, "city")
    company_id              = (By.ID, "company")
    address_id              = (By.ID, "address1")
    postal_id               = (By.ID, "postcode")
    mobile_id               = (By.ID, "phone_mobile")
    register_xp             = (By.ID, "submitAccount")
    dropdown_state_label_xp = (By.XPATH, "//div[@id='uniform-id_state']")
    customer_tab_xp         = (By.XPATH, "//a[@title='View my customer account']")
