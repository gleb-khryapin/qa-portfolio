from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TiLoginPage:
    LOGIN = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    BUTTON = (By.CSS_SELECTOR, "[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        self.driver.find_element(*self.LOGIN).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.BUTTON).click()