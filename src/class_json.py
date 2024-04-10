from abc import ABC, abstractmethod
import json


class BaseSaver(ABC):

    @abstractmethod
    def write_data(self, *args, **kwargs):
        raise NotImplementedError   # или pass

    @abstractmethod
    def read_file(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def delete_file(self, *args, **kwargs):
        raise NotImplementedError


class JSONSaver(BaseSaver):

    def __init__(self, file):
        self.file = file

    def write_data(self, data) -> None:
        '''
        Записывает данные в файл.
        indent - отступы
        ensure_ascii=False отключает принудительное форматирование текста,
        т.к. в файле много кириллицы
        '''
        with open(self.file, 'w', encoding='utf-8') as new_file:
            json.dump(data, new_file, indent=4, ensure_ascii=False)

    def read_file(self) -> None:
        ''' Метод для чтения файла '''
        with open(self.file, 'r', encoding='utf-8') as file:
            file.readline()

    def delete_file(self) -> None:
        ''' Очищает информацию в файле.
        Используем альтернативный вариант, если у нас уже открыт файл.
        f.truncate(0) # need '0' when using r+
        '''
        with open(self.file, 'r+', encoding='utf-8') as file:
            file.truncate(0)
