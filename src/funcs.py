from class_vacancies import Vacancy


def create_list_obj(list_obj) -> list:
    '''
    Создание списка экз класса Vacancy
    :param list_obj: данные для создания экз класса
    :return: list_vacancies: список экз класса
    '''

    list_vacancies = []
    for i in list_obj:
        list_vacancies.append(
            Vacancy(i.get('name'),
                    i.get('area', {}).get('name'),
                    i.get('salary').get('from') if i["salary"] is not None else 0,
                    i.get('salary').get('to') if i["salary"] is not None else 0,
                    i.get('snippet', {}).get('requirement'),
                    i.get('apply_alternate_url'),
                    ))
    return list_vacancies


def sort_salary_from(vacs_list, user_sorting_number) -> list:
    """
    Функция для списка вакансий по зарплате
    :param vacs_list: список вакансий
    :param user_sorting_number: опция сортировки
    :return: отсортированный список
    """

    if user_sorting_number == 1:
        vacs_list.sort()
        print('Выбрано: Сортировка по возрастанию зарплаты')
    if user_sorting_number == 2:
        vacs_list.sort(reverse=True)
        print('Выбрано: Сортировка по убыванию зарплаты')
    if user_sorting_number == 3:
        print('Выбрано: Без сортировки списка вакансий')
    return vacs_list
