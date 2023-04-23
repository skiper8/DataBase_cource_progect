import json


def load_json_file(filename):
    """
    Выгружает данные из заданного файла
    """
    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data
