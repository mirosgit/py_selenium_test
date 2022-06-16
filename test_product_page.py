from .product_page import Product


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = Product(browser, link)
    page.open()
    page.go_to_product_page()
    page.solve_quiz_and_get_code()
    page.basket_summary()