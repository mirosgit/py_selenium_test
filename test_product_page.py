from .product_page import Product
import pytest


@pytest.mark.parametrize('link', ["promo=offer0",
                                  "promo=offer1",
                                  "promo=offer2",
                                  "promo=offer3",
                                  "promo=offer4",
                                  "promo=offer5",
                                  "promo=offer6",
                                  "promo=offer7",
                                  "promo=offer8",
                                  "promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{link}"
    page = Product(browser, link)
    page.open()
    page.go_to_product_page()
    page.solve_quiz_and_get_code()
    page.basket_summary()