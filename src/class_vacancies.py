from abc import ABC, abstractmethod

class BaseVacancy(ABC):

    @abstractmethod
    def __init__(self, title, city, salary, description, link):
        self.title = title
        self.city = city
        self.salary = salary
        self.description = description
        self.link = link

    @abstractmethod
    def __str__(self):
        pass


class Vacancy(BaseVacancy):
    title: str  # Название вакансии
    city: str  # Город, где открыта вакансия
    salary: str  # Предлагаемая з/п от
    description: str  # Требования
    link: str  # Ссылка на вакансию

    def __init__(self, title, city, salary, description, link):
        super().__init__(title, city, salary, description, link)

    def __repr__(self):
        return f"{self.title}, {self.city}, {self.salary}, {self.description}, {self.link}"

    def __str__(self):
        return (f"Вакансия: {self.title}\nГород: {self.city}\nЗарплата: {self.salary}"
                f"\nОписание: {self.description}\nСсылка: {self.link}")

    @property
    def title_data(self):
        if self.title is not None:
            return self.title
        else:
            return "Ошибка"

    @property
    def city_data(self):
        if self.city is not None:
            return self.city
        else:
            return "Город не указан"

    @property
    def description_data(self):
        if self.description is not None:
            return self.description
        else:
            return "Отсутствует описание вакансии"

    @property
    def link_data(self):
        if self.link is not None:
            return self.link
        else:
            return "Отсутствует ссылка на вакансию"

    @property
    def get_salary(self):
        if self.salary is not None:
            return self.salary
        return 0

    @get_salary.setter
    def get_salary(self, value):
        if value is None and not isinstance(value, (float, int)):
            self.salary = 0
        else:
            self.salary = value


    def __lt__(self, other):
        ''' Метод сравнения, меньше '''
        if self.salary is not None and other.salary is not None:
            if getattr(self.salary, 'from', 0) < getattr(other.salary, 'from', 0): #self.salary["from"] < other.salary["from"]
                return True
            else:
                return False
        elif self.salary is None:
            return True
        elif other.salary is None:
            return False

    def __gt__(self, other):
        ''' Метод сравнения, больше'''
        if self.salary is not None and other.salary is not None:
            if getattr(self.salary, 'from', 0) > getattr(other.salary, 'from', 0): #self.salary["from"] > other.salary["from"]:
                return True
            else:
                return False
        elif self.salary is None:
            return False
        elif other.salary is None:
            return True

