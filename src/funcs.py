from class_vacancies import Vacancy
def create_list_obj(list_obj):
    '''
    Создание списка экз класса Vacancy
    :param list_obj: данные для создания экз класса
    :return: list_vacancies: список экз класса
    '''

    list_vacancies = []
    for item in list_obj:
        list_vacancies.append(
            Vacancy(item.get('name'),
                    item.get('area', {}).get('name'),
                    item.get('salary').get('from') if item["salary"] is not None else 0,
                    item.get('salary').get('to') if item["salary"] is not None else 0,
                    item.get('snippet', {}).get('requirement'),
                    item.get('apply_alternate_url'),
                    ))
    return list_vacancies


def sort_salary_from(vacs_list, user_sorting_number):
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