import os
import random
import string


# создаем папочку
def create_folder(event):
    # изначально название папки - награды
    try:
        os.mkdir('награды')
        return 'награды'
    # папка награды уже есть
    except FileExistsError:
        # награды + название мероприятия
        try:
            os.mkdir(f'награды {event[0]}')
            return f'награды {event[0]}'
        # награды + случайные буквы
        except FileExistsError:
            name_folder = 'награды ' + ''.join(random.choice(string.ascii_lowercase) for i in range(6))
            os.mkdir(f'{name_folder}')
            return name_folder
