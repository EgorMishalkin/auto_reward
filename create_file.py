from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os
import shutil


# красивые шрифта
headline1 = ImageFont.truetype('arialbd.ttf', size = 85)
headline2 = ImageFont.truetype('arial.ttf', size = 20)
headline3 = ImageFont.truetype('ariblk.ttf', size = 50)
headline4 = ImageFont.truetype('arial.ttf', size = 27)
headline5 = ImageFont.truetype('arialbd.ttf', size = 45)


# делаем файлек
def create_file(name_folder, type_reward, name_sur, place, reward, event, datetime):
    img = Image.open('Шаблон грамоты.png')
    idraw = ImageDraw.Draw(img)
    # о текст мой текст
    idraw.text((300, 250), type_reward, font=headline1, fill='blue')
    idraw.text((290, 370), 'награждается', font=headline2, fill='black')
    idraw.text((250, 420), name_sur, font=headline3, fill='black')
    idraw.text((250, 550), place, font=headline4, fill='black')
    idraw.text((250, 620), reward, font=headline5, fill='black')
    idraw.text((250, 700), event, font=headline2, fill='black')
    idraw.text((280, 900), datetime, font=headline4, fill='black')

    # поставьте # если не хотите видеть фотки
    img.show()
    # сохраняем фотку
    img.save(f'{name_sur}.png')

    # переносим в папку
    dest_dir = f'{os.getcwd()}\{name_folder}'

    # move method to move the file
    shutil.move(f'{name_sur}.png', dest_dir)
