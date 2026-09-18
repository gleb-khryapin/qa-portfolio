import pytest 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"

def login(driver, username, password):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


def test_success(driver):
    login(driver, "standard_user", "secret_sauce")
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
    login(driver, username, password)
    error_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="error"]')))
    assert expected_error in error_element.text