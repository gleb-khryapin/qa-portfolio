import requests
import pytest
import allure

BASE_URL = "https://jsonplaceholder.typicode.com"
pytestmark = allure.feature("API постов")



@allure.title("Получение существующего поста")
def test_get_post():
    with allure.step("Отправить GET /posts/1"):
        response = requests.get(f"{BASE_URL}/posts/1")
        data = response.json()
    allure.attach(response.text, "Тело ответа", allure.attachment_type.JSON)
    with allure.step("Проверить код ответа"):
        assert response.status_code == 200
    with allure.step("Проверить айди"):
        assert "id" in data
    with allure.step("Проверить наличие имени"):
        assert "title" in data
    with allure.step("Проверить наличие тела"):    
        assert "body" in data
    with allure.step("Проверить наличие юзер айди"):
        assert "userId" in data
    with allure.step("Проверить значение id"):
        assert data["id"] == 1

@allure.title("Получение несуществующего поста")
def test_get_wrong():
    with allure.step("Отправить GET /posts/99999"):
        response = requests.get(f"{BASE_URL}/posts/999999")
    with allure.step("Проверка статус кода"):
        assert response.status_code == 404
        assert response.json() == {}

@allure.title("Создание поста")
def test_create_post():
    with allure.step("Подготовить тело запроса"):
        payload = {"title": "Тестовый пост", "body": "Текст", "userId": 1}
    with allure.step("Отправка поста"):
        response = requests.post(f"{BASE_URL}/posts", json=payload)
        data = response.json()
    with allure.step("Проверить ответ сервера"):
        assert response.status_code == 201
        assert "id" in data
        assert data["title"] == payload["title"]

@allure.title("Получение поста с id = {post_id}")
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_posts(post_id):
    with allure.step("Отправить GET /posts/{post_id"):
        response = requests.get(f"{BASE_URL}/posts/{post_id}")
        data = response.json()
    with allure.step("Проверка статус кода и айди"):
        assert response.status_code == 200
        assert data["id"] == post_id
