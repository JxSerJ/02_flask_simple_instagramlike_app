import pytest

from app import application

params = [
    {
        "poster_name": 0,
        "poster_avatar": 0,
        "pic": 0,
        "content": 0,
        "views_count": 0,
        "likes_count": 0,
        "pk": 0
    }
]


class TestAPI:

    def test_get_all_posts_type(self):
        response = application.test_client().get('/api/posts', follow_redirects=True)
        assert type(response.json) == list, "Получен неверный тип данных при запросе всех постов"

    def test_get_post_by_pk_type(self):
        response = application.test_client().get('/api/post/1', follow_redirects=True)
        assert type(response.json) == dict, "Получен неверный тип данных при запросе одного поста"

    def test_get_all_posts_data(self):
        response = application.test_client().get('/api/posts', follow_redirects=True)
        keys_response = response.json[0].keys()
        keys_from_params = params[0].keys()
        assert keys_response == keys_from_params, "Неверный список ключей при запросе всех постов"

    def test_get_post_by_pk_data(self):
        response = application.test_client().get('/api/post/1', follow_redirects=True)
        keys_response = response.json.keys()
        keys_from_params = params[0].keys()
        assert keys_response == keys_from_params, "Неверный список ключей при запросе одного поста"
