from HW23.Develop.pages.checkout_page import CheckoutPage
from HW23.Develop.pages.login_page import LoginPage
from HW23.Develop.pages.cart_page import CartPage
from HW23.Develop.pages.inventory_page import InventoryPage
from HW23.Develop.pages.checkout_step_one import CheckoutStep1Page
from HW23.Develop.pages.checkout_step_two import CheckoutStep2Page
from HW23.Develop.pages.last_page import CheckoutFinalPage


def test_integration_auth_and_inventory(driver):
    login_page = LoginPage(driver)
    login_page.valid_login()

    assert "inventory" in driver.current_url, "Ошибка в интеграции"

    inventory = InventoryPage(driver)
    inventory.click_on_backpack_btn()
    inventory.click_on_cart_icon()

    assert "cart" in driver.current_url, "Ошибка в интеграции"

    cart = CartPage(driver)
    cart.count_products_in_cart()

    assert cart.count_products_in_cart() == 1

    checkout = CheckoutPage(driver)
    checkout.items_checkout()

    assert "checkout-step-one" in driver.current_url, "Ошибка в интеграции"

    firstCheckout = CheckoutStep1Page(driver)
    firstCheckout.fill_out_first_name("Kate")
    firstCheckout.fill_out_last_name("Bate")
    firstCheckout.fill_out_zip_code("12345")
    firstCheckout.click_continue_btn()

    assert "checkout-step-two" in driver.current_url, "Ошибка в интеграции"

    secondCheckout = CheckoutStep2Page(driver)

    assert secondCheckout.final_check_of_quantity() == 1
    assert secondCheckout.final_check_of_item() == "Sauce Labs Backpack"

    secondCheckout.click_finish_btn()

    assert "checkout-complete" in driver.current_url, "Ошибка в интеграции"

    lastPage = CheckoutFinalPage(driver)

    assert lastPage.check_complete_message() == "Thank you for your order!"
    assert lastPage.check_checkout_status() == "Checkout: Complete!"

    lastPage.return_to_home_btn()

    assert "inventory" in driver.current_url, "Ошибка в интеграции"

    print ("Finish. E2E Test is complete")