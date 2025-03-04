from pages.base_page import BasePage


class CheckoutStep2Page(BasePage):
    FINISH_BTN = "[data-test=\"finish\"]"

    def __init__(self, page):
        super().__init__(page)

    def click_finish(self):
        self.page.locator(self.FINISH_BTN).click()