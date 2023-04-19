from abc import ABC, abstractmethod
import os
import requests


class Engine(ABC):
    word = 'Python'

    @abstractmethod
    def get_request_employer(self):
        pass

    @abstractmethod
    def get_request_vacant(self, employers_list):
        pass


class HH(Engine):

    def get_request_employer(self):
        """
        Парсим компании с ресурса HeadHunter
        """
        my_auth_data = {'X-Api-App-Id': os.environ['HH_API_KEY']}
        url = 'https://api.hh.ru/vacancies?text=' + self.word
        employers_list = []
        for item in range(10):
            request_hh = requests.get(url, headers=my_auth_data,
                                      params={"keywords": self.word, 'page': item}).json()['items']
            for item2 in request_hh:
                if len(employers_list) == 10:
                    break
                if item2 in employers_list:
                    continue
                employers_list.append(item2['employer']['name'])
        return employers_list

    def get_request_vacant(self, employers_list):
        """
        Парсим данные по комнанияс с ресурса HeadHunter
        """
        vacancies_list_hh = []
        for word in employers_list:
            my_auth_data = {'X-Api-App-Id': os.environ['HH_API_KEY']}
            url = 'https://api.hh.ru/vacancies?text=' + word
            for item in range(1):
                request_hh = requests.get(url, headers=my_auth_data,
                                          params={"keywords": word, 'page': item}).json()['items']
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


i = HH()
employers_list = i.get_request_employer()
print(employers_list)
vacants = i.get_request_vacant(employers_list)
for i in vacants:
    if i['employer']['name'] == 'Spectr':
        print(i['employer']['name'])
