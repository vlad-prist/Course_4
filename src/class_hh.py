from abc import ABC, abstractmethod
import requests
class Base_HH(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        pass

class HeadHunter(Base_HH):

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {'text': '', 'page': 0, 'per_page': 10, 'area': 113}
        self.vacancies = []

    def get_vacancies(self, keyword):
        '''
        Функция получения вакансий с апишки по пользовательскому слову
        :param keyword: Слово для поиска вакансии, которе вводит пользователь
        :return: возвращает список вакансий
        '''
        self.params['text'] = keyword
        while self.params.get('page') != 2:
            response = requests.get(self.url, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies

''' закоментен иной вариант распаковки апишки'''
        # url = 'https://api.hh.ru/vacancies'
        # params = {'text': keyword, 'per_page': 10, 'area': '113'}
        # response = requests.get(url, params=params)  # 'area': '113' - Россия
        # data = response.json()
        # return data