from selenium.webdriver.common.by import By
from HW23.Develop.pages.base_page import BasePage


class CheckoutStep1Page(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")

    def fill_out_first_name(self, firstName):
        self.enter_text(self.FIRST_NAME, firstName)

    def fill_out_last_name(self, lastName):
        self.enter_text(self.LAST_NAME, lastName)

    def fill_out_zip_code(self, zipCode):
        self.enter_text(self.ZIP_CODE, zipCode)

    def click_continue_btn(self):
        self.click_element(self.CONTINUE_BTN)
