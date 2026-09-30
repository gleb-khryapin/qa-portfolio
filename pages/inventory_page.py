from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    TITLE = (By.CSS_SELECTOR, ".title")
    ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")            


    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        wait = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.TITLE))
        return wait.text
    def get_count(self):
        count = self.driver.find_elements(*self.ITEM_NAME)
        return len(count)                            
