from playwright.sync_api import expect
from pages.cart_page import CartPage
from pages.checkout_step1_page import CheckoutStep1Page
from pages.checkout_step2_page import CheckoutStep2Page
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.complete_order_page import LastPage


def test_make_an_order(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_step1 = CheckoutStep1Page(page)
    checkout_step2 = CheckoutStep2Page(page)
    final_page = LastPage(page)
    login_page.logged_user()

    expect(page.locator(inventory_page.CART_ICON)).to_be_visible()

    inventory_page.add_item_to_cart()
    inventory_page.open_cart()


    expect(page.locator(cart_page.ITEM_QUANTITY)).to_contain_text("1")
    expect(page.locator(cart_page.ITEM_NAME)).to_contain_text("Sauce Labs Backpack")

    cart_page.move_to_checkout()

    checkout_step1.fill_in_First_Name("Kate")
    checkout_step1.fill_in_Last_Name("Test")
    checkout_step1.fill_in_Zip_Code("1233")
    checkout_step1.continue_checkout()

    checkout_step2.click_finish()

    expect(page.locator(final_page.COMPLETE_HEADER)).to_contain_text("Thank you for your order!")
    final_page.return_home()


