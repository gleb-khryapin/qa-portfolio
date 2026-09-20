import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
pytestmark = pytest.mark.skip(reason="Сайт нестабилен, тесты переносим на saucedemo")


DISH_URL = "https://bison44.ru/kostroma/popular/v-syrnom-lavashe-kurinaya"


def test_title_contains_bison(driver):
    driver.get("https://bison44.ru/kostroma")
    WebDriverWait(driver, 15).until(EC.title_contains("БИЗОН"))
    assert "БИЗОН" in driver.title

@pytest.mark.skip(reason="Уточняем локатор названия: .product-options__title даёт 3 элемента")
def test_dish_page_shows_name(driver):
    driver.get(DISH_URL)
    name = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, div.calories__value))
    )
    assert "лаваш" in name.text.lower()


def test_dish_has_nutrition_block(driver):
    driver.get(DISH_URL)
    values = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".calories__value"))
    )
    assert len(values) > 0



@pytest.mark.xfail(reason="BUG-002: пищевая ценность 0/0/0", raises=AssertionError)
def test_dish_nutrition_not_zero(driver):
    driver.get(DISH_URL)
    values = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".calories__value"))
    )
    numbers = [v.text.strip() for v in values]
    assert not all(n == "0" for n in numbers)

def test_debug_dish_page(driver):
    driver.get(DISH_URL)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".product-options__title"))
    )
    driver.save_screenshot("debug_dish.png")

    titles = driver.find_elements(By.CSS_SELECTOR, ".product-options__title")
    print("\nЗАГОЛОВКИ:", [t.text for t in titles])

    calories = driver.find_elements(By.CSS_SELECTOR, ".calories__value")
    print("КАЛОРИИ:", len(calories), [c.text for c in calories])
