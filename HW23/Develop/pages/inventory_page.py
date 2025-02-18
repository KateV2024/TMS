from selenium.webdriver.common.by import By
from HW23.Develop.pages.base_page import BasePage


class InventoryPage(BasePage):
    BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def click_on_backpack_btn(self):
        self.click_element(self.BACKPACK_BTN)

    def click_on_cart_icon(self):
        self.click_element(self.CART_ICON)
