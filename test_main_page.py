from .main_page import MainPage
from .login_page import LoginPage
from selenium.webdriver.common.by import By


def test_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/de/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


def test_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/de/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/de/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()