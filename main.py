from PIL import Image, ImageFilter, ImageDraw, ImageFont
import pandas
import os
import shutil
import random
import string

data = pandas.read_excel('1.xlsx', sheet_name='Лист1')

type = data['Вид грамоты'].tolist()
name_sur = data['ФИ участника'].tolist()
place = data['Наименование организатора мероприятия'].tolist()
reward = data['Место/награда/номинация'].tolist()
event = data['Название мероприятия'].tolist()
datetime = data['Дата проведения'].tolist()
name_folder = ''

try:
    os.mkdir('награды')
    name_folder = 'награды'
except FileExistsError:
    try:
        name_folder = f'награды {event[0]}'
        os.mkdir(f'награды {event[0]}')
    except FileExistsError:
        name_folder = 'награды ' + ''.join(random.choice(string.ascii_lowercase) for i in range(6))
        os.mkdir(f'{name_folder}')

headline = ImageFont.truetype('arialbd.ttf', size=30)


for i in range(len(name_sur)):
    img = Image.open('Шаблон грамоты.png')
    idraw = ImageDraw.Draw(img)
    idraw.text((300, 300), type[i], font=headline, fill='blue')
    idraw.text((300, 400), 'награждается', font=headline, fill='black')
    idraw.text((250, 500), name_sur[i], font=headline, fill='black')
    idraw.text((250, 600), place[i], font=headline, fill='black')
    idraw.text((250, 720), reward[i], font=headline, fill='black')
    idraw.text((250, 800), event[i], font=headline, fill='black')
    idraw.text((250, 900), str(datetime[i]), font=headline, fill='black')

    # img.show()
    img.save(f'{name_sur[i]}.png')

    dest_dir = f'{os.getcwd()}\{name_folder}'
    # img.save(f'{dest_dir}\{name_sur[i]}.png')

    # move method to move the file
    shutil.move(f'{name_sur[i]}.png', dest_dir)
