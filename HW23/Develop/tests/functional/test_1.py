import pytest
from HW23.Develop.pages.login_page import LoginPage

def test_empty_fields(driver):
    login_page = LoginPage(driver)
    login_page.get_login_page()
    login_page.click_login()
    login_page.get_error_message()

    assert login_page.get_error_message() == "Epic sadface: Username is required", 'Неверно'
