from pages.base_page import BasePage


class InventoryPage(BasePage):

    CART_ICON = "[data-test='shopping-cart-link']"
    ADD_SAUCE_BACKPACK = "[data-test=\"add-to-cart-sauce-labs-backpack\"]"


    def __init__(self, page):
        super().__init__(page)

    def add_item_to_cart(self):
        self.page.locator(self.ADD_SAUCE_BACKPACK).click()

    def open_cart(self):
        self.page.locator(self.CART_ICON).click()
