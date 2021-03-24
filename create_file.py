from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os
import shutil
from docx2pdf import convert
from pdf_work import write_to_file


# делаем файлек
def create_file(name_folder, dox_place, type_reward, name_sur, place, reward, event, datetime):
    convert(dox_place, "шаблон грамоты.pdf")
    write_to_file(f'{name_sur}.pdf', 'шаблон грамоты.pdf', [type_reward, name_sur, place, reward, event, datetime])
    dest_dir = f'{os.getcwd()}\{name_folder}'
    shutil.move(f'{name_sur}.pdf', dest_dir)

    # sum_file(f'{name_sur}.pdf', 'шаблон грамоты.pdf', 'merged.pdf')

