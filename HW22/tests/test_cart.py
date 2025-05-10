from HW22.pages.cart_page import CartPage
from HW22.pages.login_page import LoginPage
from HW22.pages.inventory_page import InventoryPage


def test_checkout(driver):
    login_page = LoginPage(driver)
    login_page.logged_user()

    assert "inventory" in driver.current_url, "Ошибка: логин не удался"

    product_page = InventoryPage(driver)

    product_page.click_on_backpack_btn()
    product_page.click_on_tshirt_btn()
    product_page.click_on_cart_icon()

    assert "cart" in driver.current_url, "Ошибка, юзер не попал в корзину"

    cart = CartPage(driver)
    assert cart.count_products_in_cart() == 2, "Ошибка, в корзине не находится 2 товара"





