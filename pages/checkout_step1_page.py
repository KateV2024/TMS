from pages.base_page import BasePage


class CheckoutStep1Page(BasePage):
    FIRST_NAME = "[data-test=\"firstName\"]"
    LAST_NAME = "[data-test=\"lastName\"]"
    ZIP_CODE = "[data-test=\"postalCode\"]"
    CONTINUE_BTN = "[data-test=\"continue\"]"

    def __init__(self, page):
        super().__init__(page)

    def fill_in_First_Name(self, firstName):
        self.page.locator(self.FIRST_NAME).fill(firstName)

    def fill_in_Last_Name(self, lastName):
        self.page.locator(self.LAST_NAME).fill(lastName)

    def fill_in_Zip_Code(self, zipCode):
        self.page.locator(self.ZIP_CODE).fill(zipCode)

    def continue_checkout(self):
        self.page.locator(self.CONTINUE_BTN).click()