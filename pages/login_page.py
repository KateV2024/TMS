from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = "[data-test=\"username\"]"
    PASSWORD_INPUT = "[data-test=\"password\"]"
    LOGIN_BUTTON = "[data-test=\"login-button\"]"

    def __init__(self, page):
        super().__init__(page)  # Fixed 'super()' call

    def go_to_url(self):
        self.page.goto("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.page.locator(self.USERNAME_INPUT).fill(username)

    def enter_password(self, password):
        self.page.locator(self.PASSWORD_INPUT).fill(password)  # Fix argument here

    def click_login(self):
        self.page.locator(self.LOGIN_BUTTON).click()

    def logged_user(self):
        self.page.goto("https://www.saucedemo.com/")
        self.page.locator(self.USERNAME_INPUT).fill("standard_user")
        self.page.locator(self.PASSWORD_INPUT).fill("secret_sauce")
        self.page.locator(self.LOGIN_BUTTON).click()
