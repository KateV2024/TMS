from pages.base_page import BasePage


class CartPage(BasePage):
    ITEM_QUANTITY = "[data-test=\"item-quantity\"]"
    ITEM_NAME = "[data-test=\"inventory-item-name\"]"
    CHECKOUT_BTN = "[data-test=\"checkout\"]"

    def __init__(self, page):
        super().__init__(page)

    def move_to_checkout(self):
        self.page.locator(self.CHECKOUT_BTN).click()

