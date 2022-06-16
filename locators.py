from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    Log_Email_ID = (By.ID, "id_login-username")
    Log_Pass_ID = (By.ID, "id_login-password")
    Reg_Email_ID = (By.ID, "id_registration-email")
    Reg_Pass_ID = (By.ID, "id_registration-password1")
    Reg_Rep_Pass_ID = (By.ID, "id_registration-password2")


class ProductPageLocators():
    Basket_CLASS = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    Alert_Basket_CSS = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    Name_Product_CSS = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")