import pandas
from create_folder import create_folder
from create_file import create_file


def get_info(filename, dox_place):
    # получаем всю всю информацию из excel файла
    data = pandas.read_excel(filename, sheet_name='Лист1')

    try:
        # делаем ччф формат для данных
        type_reward = data['Вид грамоты'].tolist()
        name_sur = data['ФИ участника'].tolist()
        place = data['Наименование организатора мероприятия'].tolist()
        reward = data['Место/награда/номинация'].tolist()
        event = data['Название мероприятия'].tolist()
        datetime = data['Дата проведения'].tolist()

        # создаем папку, в которую будем помещать фотографии
        name_folder = create_folder(event)

        # передаем данные в функцию, где создаются дипломы
        for i in range(len(name_sur)):
            create_file(name_folder, dox_place, type_reward[i], name_sur[i], place[i], reward[i], event[i], datetime[i])
        return 'ok'
    except KeyError:
        return 'key_error'
