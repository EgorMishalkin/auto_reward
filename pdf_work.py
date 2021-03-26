from reportlab.pdfgen.canvas import Canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os


def write_to_file(filename, story):
    # файл, который получится при соединении
    output = filename.split(".pdf")[0] + ".pdf"
    print(output)
    # шаблон грамоты
    template = 'shablon_gramoty.pdf'
    # файл, который делается по информации из таблицы
    title = filename
    canvas = Canvas(title)
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
    # Тут его читаешь

    f1 = open(template, 'rb')
    f_pdf = PdfFileReader(f1)
    f2 = open(title, 'rb')
    s_pdf = PdfFileReader(f2)
    # Собираешь из двух файлов один
    page = f_pdf.getPage(0)
    page.mergePage(s_pdf.getPage(0))

    # записываешь конечный файл
    output_file = PdfFileWriter()
    output_file.addPage(page)

    with open(output, 'wb') as f:
        output_file.write(f)

    f1.close()
    f2.close()
    os.remove(title)
