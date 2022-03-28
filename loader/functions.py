import json


def add_post_into_json(path: str, data_to_add: tuple[str, str]) -> None:

    data_to_insert = {"pic": data_to_add[0], "content": data_to_add[1]}
    with open(path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        data.insert(0, data_to_insert)
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(data, file, ensure_ascii=False)
