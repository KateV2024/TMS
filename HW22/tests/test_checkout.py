from HW22.pages.cart_page import CartPage
from HW22.pages.login_page import LoginPage
from HW22.pages.inventory_page import InventoryPage
from HW22.pages.checkout_page import CheckoutPage


def test_cart(driver):
    login_page = LoginPage(driver)
    login_page.logged_user()

    assert "inventory" in driver.current_url, "Ошибка: логин не удался"

    product_page = InventoryPage(driver)

    product_page.click_on_backpack_btn()
    product_page.click_on_tshirt_btn()
    product_page.click_on_cart_icon()

    assert "cart" in driver.current_url, "Ошибка"

    cart = CartPage(driver)
    assert cart.count_products_in_cart() == 2

    checkout = CheckoutPage(driver)
    checkout.items_checkout()

    assert "checkout-step-one" in driver.current_url, "Ошибка"


