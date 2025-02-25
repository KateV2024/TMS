from pages.base_page import BasePage


class LastPage(BasePage):
    COMPLETE_HEADER = "[data-test=\"complete-header\"]"
    HOME_BTN = "[data-test=\"back-to-products\"]"

    def __init__(self, page):
        super().__init__(page)

    def return_home(self):
        self.page.locator(self.HOME_BTN).click()