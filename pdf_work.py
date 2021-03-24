import PyPDF2 as pypdf
import os
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
from fpdf import FPDF


#def sum_file(pdf_file, watermark, merged):
#    with open(pdf_file, "rb") as input_file, open(watermark, "rb") as watermark_file:
#        input_pdf = PdfFileReader(input_file)
#        watermark_pdf = PdfFileReader(watermark_file)
#        watermark_page = watermark_pdf.getPage(0)
#
#        output = PdfFileWriter()
#
#        for i in range(input_pdf.getNumPages()):
#            pdf_page = input_pdf.getPage(i)
#            pdf_page.mergePage(watermark_page)
#            output.addPage(pdf_page)
#
#        with open(merged, "wb") as merged_file:
#            output.write(merged_file)
#
#
#def write_to_file(filename, story):
#    canvas = Canvas(filename, pagesize=A4)
#    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
#    canvas.setFont('FreeSans', 50)
#    canvas.setFillColor('blue')
#    canvas.setFont('FreeSans', 30)
#    canvas.drawString(150, 600, story[0])
#    canvas.setFillColor('black')
#    canvas.drawString(100, 500, story[1])
#    canvas.drawString(100, 400, story[2])
#    canvas.drawString(100, 300, story[3])
#    canvas.drawString(100, 200, story[4])
#    canvas.drawString(150, 50, story[5])
#    canvas.showPage()
#    canvas.save()


def write_to_file(filename, template, story):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 100, txt="qwerty", ln=1, align="C")
    pdf.output(filename)
    with open(template, "rb") as inFile, open(filename, "rb") as overlay:
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
