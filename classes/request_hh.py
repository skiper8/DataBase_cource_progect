from abc import ABC, abstractmethod
import requests
import time
import json


class Engine(ABC):
    word = 'Python'

    @abstractmethod
    def get_request_company(self):
        pass

    @abstractmethod
    def get_request_vacantcies(self, employers_list):
        pass


class HH(Engine):

    def get_request_company(self):
        """
        Парсим компании с ресурса HeadHunter
        """
        url = 'https://api.hh.ru/vacancies?text=' + self.word
        company_id = []
        company_list = []
        for item in range(10):
            request_hh = requests.get(url, params={"keywords": self.word}).json()['items']
            time.sleep(0.5)
            for item2 in request_hh:
                if len(company_list) == 10:
                    break
                if item2 in company_list:
                    continue
                company_list.append({"employer_id": item2['employer']['id'],
                                     "employer_name": item2['employer']['name']})
                company_id.append(item2['employer']['id'])
        return company_list, company_id

    def get_request_vacantcies(self, company_id):
        """
        Парсим данные по комнанияс с ресурса HeadHunter
        """
        vacancies_list_hh = []
        for id in company_id:
            url = 'https://api.hh.ru/vacancies?' + str(id)
            for item in range(10):
                request_hh = requests.get(url, params={"employer_id": str(id)}).json()['items']
                time.sleep(0.5)
                for item2 in request_hh:
                    if item2["salary"] is None:
                        item2["salary"] = {}
                        item2["salary"]["from"] = 0
                        item2["salary"]["to"] = 0
                    if item2["salary"]["from"] is None:
                        item2["salary"]["from"] = 0
                    if item2["salary"]["to"] is None:
                        item2["salary"]["to"] = 0
                    if item2["salary"]["from"] > item2["salary"]["to"]:
                        tmp = item2["salary"]["from"]
                        item2["salary"]["from"] = item2["salary"]["to"]
                        item2["salary"]["to"] = tmp
                    vacancies_list_hh.append(item2)
        return vacancies_list_hh

    def insert_vacancies(self, data):
        """
        Запись данных о вакансиях в файл с сохранением структуры и исходных данных
        """
        vacant_hh = []
        with open('vacantes.json', "w", encoding='UTF-8') as file:
            for i in range(len(data)):
                vacant_hh.append(
                    {
                        "source": 'HeadHunter',
                        "name": data[i]['name'],
                        "description": data[i]['snippet']['responsibility'],
                        "url": data[i]['alternate_url'],
                        "city": data[i]["area"]["name"],
                        "employer_name": data[i]['employer']['name'],
                        "employer_id": data[i]['employer']['id'],
                        "salary_from": data[i]["salary"]["from"],
                        "salary_to": data[i]["salary"]["to"],
                        "date": data[i]['published_at']
                    }
                )
            json.dump(vacant_hh, file, indent=4, ensure_ascii=False)
        return vacant_hh

    def insert_company(self, data):
        """
        Запись данных компаний в файл с сохранением структуры и исходных данных
        """
        company_hh = []
        with open('companys.json', "w", encoding='UTF-8') as file:
            for i in range(len(data)):
                company_hh.append(
                    {
                        "employer_name": data[i]['employer_name'],
                        "employer_id": data[i]['employer_id']

                    }
                )
            json.dump(company_hh, file, indent=4, ensure_ascii=False)
        return company_hh
