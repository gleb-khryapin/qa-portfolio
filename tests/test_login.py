import pytest 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_success(driver):
    inv_page = InventoryPage(driver)
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    check_title = inv_page.get_title()
    check_count = inv_page.get_count()
    assert "Products" in check_title
    assert check_count == 6
    assert "inventory.html" in driver.current_url


@pytest.mark.parametrize("username, password, expected_error",[
    ("locked_out_user", "secret_sauce", "locked out"),   
    ("standard_user", "wrong_password", "do not match"),
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "", "Password is required"),
])
def test_login_errors(driver, username, password, expected_error):    
    page = LoginPage(driver)
    page.open()
    page.login(username, password)
    assert expected_error in page.get_error_text()