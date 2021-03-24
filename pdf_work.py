from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def write_to_file(filename, story):

    canvas = Canvas(filename, pagesize=A4)
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    canvas.setFont('FreeSans', 30)
    #
    canvas.drawString(150, 600, story[0])
    canvas.drawString(100, 500, story[1])
    canvas.drawString(100, 400, story[2])
    canvas.drawString(100, 300, story[3])
    canvas.drawString(100, 200, story[4])
    canvas.drawString(150, 50, story[5])

    canvas.showPage()
    canvas.save()
