import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert response.status_code == 200
    assert "id" in data
    assert "title" in data
    assert "body" in data
    assert "userId" in data
    assert data["id"] == 1


def test_get_wrong():
    response = requests.get(f"{BASE_URL}/posts/999999")
    data = response.json()

    assert response.status_code == 404
    assert response.json() == {}

def test_create_post():
    payload = {"title": "Тестовый пост", "body": "Текст", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    data = response.json()

    assert response.status_code == 201
    assert "id" in data
    assert data["title"] == payload["title"]


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_posts(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == post_id
