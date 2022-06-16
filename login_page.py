from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        #self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

  #  def should_be_login_url(self):
  #      self.browser.current_url("http://selenium1py.pythonanywhere.com/de/accounts/login/")

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.Log_Email_ID), "Login Email is not presented"
        assert self.is_element_present(*LoginPageLocators.Log_Pass_ID), "Login Password is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.Reg_Email_ID), "Register Email is not presented"
        assert self.is_element_present(*LoginPageLocators.Reg_Pass_ID), "Register Password is not presented"
        assert self.is_element_present(*LoginPageLocators.Reg_Rep_Pass_ID), "Register Repeat Password is not presented"
