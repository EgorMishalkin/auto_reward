import pandas
from create_folder import create_folder
from create_file import create_file

# получаем всю всю информацию из excel файла
data = pandas.read_excel('1.xlsx', sheet_name='Лист1')

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
    create_file(name_folder, type_reward[i], name_sur[i], place[i], reward[i], event[i], datetime[i])
