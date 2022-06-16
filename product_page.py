from .base_page import BasePage
from .locators import ProductPageLocators


class Product(BasePage):
    def go_to_product_page(self):
        link = self.browser.find_element(*ProductPageLocators.Basket_CLASS)
        link.click()

    def basket_summary(self):
        assert self.browser.find_element(*ProductPageLocators.Alert_Basket_CSS), "Alert Name Product  Not Found :("
        assert self.browser.find_element(*ProductPageLocators.Name_Product_CSS), "Name Product  Not Found :("
        alert_basket = self.browser.find_element(*ProductPageLocators.Alert_Basket_CSS).text
        name_basket = self.browser.find_element(*ProductPageLocators.Name_Product_CSS).text
        assert str(alert_basket) == str(name_basket), "Different names"