import pytest

from app import application

params = [
    {
        "poster_name": "leo",
        "poster_avatar": "https://randus.org/avatars/w/c1819dbdffffff18.png",
        "pic": "https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
        "content": "Ага, опять #еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.",
        "views_count": 376,
        "likes_count": 154,
        "pk": 1
    },
    {
        "poster_name": "johnny",
        "poster_avatar": "https://randus.org/avatars/m/00183c7e3c382499.png",
        "pic": "https://images.unsplash.com/photo-1592660716763-09efba6db4e3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
        "content": "Вышел погулять днем, пока все на работе. На улице странные штуки, похожие на колонны, которые кто-то сгрыз – незаметно и аккуратно, так, что даже мусора не осталось. И еще много странного: например, почему-то все птицы летают, как птицы, и, похоже, им это совершенно не мешает. Или вот еще: в траве – как будто следы от чьих-то ног, хотя вроде бы я ходил довольно тихо... На следующий день было совсем пусто. Я вышел и почувствовал себя очень одиноко. Пошел к остановке. Вокруг было много народу – и все одинаковые. Как будто все они приехали сюда из одного дома и вышли на этом перекрестке после работы, чтобы не возвращаться в свои квартиры.",
        "views_count": 233,
        "likes_count": 101,
        "pk": 2
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
