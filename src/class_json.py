from abc import ABC, abstractmethod
import json

class BaseSaver(ABC):

    @abstractmethod
    def write_data(self, *args, **kwargs):
        raise NotImplementedError   # или pass

    @abstractmethod
    def delete_file(self, *args, **kwargs):
        raise NotImplementedError

class JSONSaver(BaseSaver):

    def __init__(self, file):
        self.file = file

    def write_data(self, data) -> None:
        ''' Записывает данные в файл '''
        with open(self.file, 'w', encoding='utf-8') as new_file:
            json.dump(data, new_file, indent=4, ensure_ascii=False)
            #indent - отступы
            #ensure_ascii=False отключает принудительное форматирование текста, т.к. в файле много кириллицы

    def delete_file(self) -> None: #ничего не возвращает
        ''' Очищает информацию в файле '''
        with open(self.file, 'w', encoding='utf-8') as file:
            file.write('')