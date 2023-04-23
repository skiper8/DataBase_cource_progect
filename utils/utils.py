import json


def load_json_vacancies(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data

