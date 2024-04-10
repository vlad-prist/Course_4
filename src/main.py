from class_hh import HeadHunter
from class_json import JSONSaver
from funcs import create_list_obj, sort_salary_from


def user_interaction():
    ''' Функция для взаимодействия с пользователем '''
    print("Добро пожаловать! "
          "Данное приложение поможет вам найти интересующую вас вакансию.")
    user_vacancy = input("Введите интересующую вас вакансию: ").lower().strip()
    hh = HeadHunter()
    vacancy_from_hh = hh.get_vacancies(user_vacancy)
    saving_vac = JSONSaver("../data/searching_vacs.json")
    saving_vac.write_data(vacancy_from_hh)
    user_sorting_number = int(input('Наберите номер для сортировки списка '
                                    'вакансий:\n'
                                    '1 - сортировка по возрастанию зарплаты\n'
                                    '2 - сортировка по убыванию зарплаты\n'
                                    '3 - без сортировки\n'))

    # конвертирование в список
    vacs_list = create_list_obj(vacancy_from_hh)

    # Сортировка вакансий
    sorted_vacs = sort_salary_from(vacs_list, user_sorting_number)

    # Вывод топ-вакансий по желанию пользователя
    user_top_number = int(input('Выберите топ-список вакансий для вывода на '
                                'экран (нажмите соответсвующую цифру):\n'
                                '1 - топ-5 вакансий\n'
                                '2 - топ-10 вакансий\n'
                                '3 - топ-15 вакансий\n'
                                '4 - показать все вакансии\n'))
    if user_top_number == 1:
        for vac in sorted_vacs[:5]:
            print(vac)
    elif user_top_number == 2:
        for vac in sorted_vacs[:10]:
            print(vac)
    elif user_top_number == 3:
        for vac in sorted_vacs[:15]:
            print(vac)
    elif user_top_number == 4:
        for vac in sorted_vacs:
            print(vac)

    # Завершение программы или запуск сначала
    choose_another_vac = input("Хотите выбрать другую вакансию?\n "
                               "y/n : \n").lower().strip()
    if choose_another_vac in ['y', 'yes', 'да', 'д']:

        user_interaction()
    elif choose_another_vac in ['n', 'no', 'нет', 'н']:
        print('Программа завершена. Удачи!')
        saving_vac.delete_file()
        exit()


if __name__ == "__main__":
    user_interaction()
