from selenium.webdriver.common.by import By
from HW22.pages.base_page import BasePage


class CartPage(BasePage):
    ITEMS_IN_CART = (By.CLASS_NAME, 'cart_item')


    def count_products_in_cart(self):
        return len(self.driver.find_elements(*self.ITEMS_IN_CART))
