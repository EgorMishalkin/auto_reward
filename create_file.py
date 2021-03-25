from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os
import shutil
from docx2pdf import convert
from pdf_work import write_to_file


# красивые шрифта
headline1 = ImageFont.truetype('arialbd.ttf', size=85)
headline2 = ImageFont.truetype('arial.ttf', size=40)
headline3 = ImageFont.truetype('ariblk.ttf', size=50)
headline4 = ImageFont.truetype('arial.ttf', size=27)
headline5 = ImageFont.truetype('arialbd.ttf', size=45)


# делаем файлек
def create_file(name_folder, dox_place, type_reward, name_sur, place, reward, event, datetime):
    # convert("шаблон грамоты.docx")
    # convert("шаблон грамоты.docx", "output.pdf")
    # os.rename('шаблон грамоты.pdf', f'{name_sur}.pdf')
    convert(dox_place)
    convert(dox_place, "output.pdf")
    os.rename(f'{dox_place.split(".")[0]}.pdf', f'{name_sur}.pdf.pdf')

    # convert("my_docx_folder/")
    write_to_file(f'{name_sur}.pdf.pdf', [type_reward, name_sur, place, reward, event, datetime])

    dest_dir = f'{os.getcwd()}\{name_folder}'
    # move method to move the file
    shutil.move(f'{name_sur}.pdf', dest_dir)

   # sum_file(f'{name_sur}.pdf', 'шаблон грамоты.pdf', f'{name_sur}.pdf')

