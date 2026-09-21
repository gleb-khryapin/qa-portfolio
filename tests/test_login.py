import pytest 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

def test_success(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    title = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title")))
    assert "Products" in title.text
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