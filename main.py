from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


# укажи название всех файлов
# файл, который получится при соединении
output = 'out.pdf'
# шаблон грамоты
template = 'shablon_gramoty.pdf'
# файл, который делается по информации из таблицы
title = 'title.pdf'

# конвертни шаблон из дока в пдф
# convert_to_pdf(filename=template)

# Тут его читаешь
f_pdf = PdfFileReader(open(template, 'rb'))


# Создаешь надпись "награждается"
# сюда добавить русский текст
canvas = canvas.Canvas(title)
story = ['егор', 'dd0', '110', 'антон', 'коля', 'dd']
pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
canvas.setFont('FreeSans', 50)
canvas.setFillColor('blue')
canvas.setFont('FreeSans', 30)
canvas.drawString(200, 650, story[0])
canvas.setFillColor('black')
canvas.drawString(200, 500, story[1])
canvas.drawString(200, 400, story[2])
canvas.drawString(200, 300, story[3])
canvas.drawString(200, 200, story[4])
canvas.drawString(200, 50, story[5])
canvas.showPage()
canvas.save()


# Читаешь пдф с надписью
s_pdf = PdfFileReader(open(title, 'rb'))
# Собираешь из двух файлов один
page = f_pdf.getPage(0)
page.mergePage(s_pdf.getPage(0))

# записываешь конечный файл
output_file = PdfFileWriter()
output_file.addPage(page)

with open(output, 'wb') as f:
    output_file.write(f)


# удаляешь все ненужные файлы:
# 1. файл пдф шаблон
# 2. файл с надписью
