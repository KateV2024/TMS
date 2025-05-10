from selenium.webdriver.common.by import By
from HW23.Develop.pages.base_page import BasePage


class CartPage(BasePage):
    PRODUCTS_IN_CART = (By.CLASS_NAME, 'cart_list')

    def count_products_in_cart(self):
        return len(self.driver.find_elements(*self.PRODUCTS_IN_CART))