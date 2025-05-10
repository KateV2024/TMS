from selenium.webdriver.common.by import By
from HW23.Develop.pages.base_page import BasePage


class CheckoutFinalPage(BasePage):
    BACK_HOME_BTN = (By.ID, "back-to-products")
    COMPLETE_CHECKOUT = (By.CLASS_NAME, "title")
    COMPLETE_MESSAGE = (By.CLASS_NAME, "complete-header")

    def check_checkout_status(self):
        return self.find_element(self.COMPLETE_CHECKOUT).text

    def check_complete_message(self):
        return self.find_element(self.COMPLETE_MESSAGE).text

    def return_to_home_btn(self):
        self.click_element(self.BACK_HOME_BTN)