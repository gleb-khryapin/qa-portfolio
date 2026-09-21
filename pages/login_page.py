
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    LOGIN = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    BUTTON = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, '[data-test="error"]')
    

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element(*self.LOGIN).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.BUTTON).click()

    def get_error_text(self):
        error_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ERROR))

        return error_element.text
