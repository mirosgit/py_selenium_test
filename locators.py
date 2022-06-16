from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    Log_Email_ID = (By.ID, "id_login-username")
    Log_Pass_ID = (By.ID, "id_login-password")
    Reg_Email_ID = (By.ID, "id_registration-email")
    Reg_Pass_ID = (By.ID, "id_registration-password1")
    Reg_Rep_Pass_ID = (By.ID, "id_registration-password2")