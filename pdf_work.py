import PyPDF2 as pypdf
import os
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
from fpdf import FPDF
def write_to_file(filename, story):
    canvas = Canvas(filename, pagesize=A4)
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
    all(filename, story)


def  all(filename, story):
    with open("shablon_gramoty.pdf", "rb") as inFile, open(filename, "rb") as overlay:
        original = pypdf.PdfFileReader(inFile)
        background = original.getPage(0)
        foreground = pypdf.PdfFileReader(overlay).getPage(0)

        # merge the first two pages
        background.mergePage(foreground)

        # add all pages to a writer
        writer = pypdf.PdfFileWriter()
        for i in range(original.getNumPages()):
            page = original.getPage(i)
            writer.addPage(page)

        # write everything in the writer to a file
        with open(filename, "wb") as outFile:
            writer.write(outFile)
