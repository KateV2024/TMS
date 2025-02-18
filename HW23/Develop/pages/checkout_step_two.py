from selenium.webdriver.common.by import By
from HW23.Develop.pages.base_page import BasePage


class CheckoutStep2Page(BasePage):
    FINISH_BTN = (By.ID, "finish")
    BACKPACK_QUANTITY = (By.CLASS_NAME, "cart_quantity")
    ITEM = (By.CLASS_NAME, "inventory_item_name")

    def click_finish_btn(self):
        self.click_element(self.FINISH_BTN)

    def final_check_of_quantity(self, ):
        return int(self.find_element(self.BACKPACK_QUANTITY).text)

    def final_check_of_item(self):
        return self.find_element(self.ITEM).text