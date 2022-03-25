import json

__data = []


def load_json_file(path: str) -> list:
    """
    JSON Data loader

    :param path: data-file path
    :return: data
    """
    global __data
    with open(path, 'r', encoding='utf-8') as file:
        __data = json.load(file)
    return __data


def upload_into_json_file(path: str, data: list) -> None:
    """
    JSON Data uploader

    :param data: data to upload into JSON-file
    :param path: data-file path
    :return: None
    """
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)
