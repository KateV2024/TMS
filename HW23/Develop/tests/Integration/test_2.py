import pytest
from HW23.Develop.pages.login_page import LoginPage


def test_integration_auth_and_inventory(driver):
    login_page = LoginPage(driver)
    login_page.valid_login()

    assert "inventory" in driver.current_url, "Ошибка в интеграции, юзер не авторизован"

