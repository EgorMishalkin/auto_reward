from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Frame
from reportlab.graphics.shapes import Drawing, Line
from reportlab.pdfgen.canvas import Canvas


def write_to_file(filename, story):
    """
    (str, list) -> None

    Write text from list of strings story to filename. filename should be in format name.pdf.
    Russian text is supported by font DejaVuSerif. DejaVuSerif.ttf should be saved in the working directory.
    filename is stored in the same working directory. 
    """

    canvas = Canvas(filename)
    pdfmetrics.registerFont(TTFont('arial', 'arial.ttf'))

    # Various styles option are available, consult reportlab User Guide
    style = ParagraphStyle('russian_text')
    style.fontName = 'arial'
    style.leading = 0.5*cm

    # Using XML format for new line character
    for i, part in enumerate(story):
        story[i] = Paragraph(part.replace('\n', '<br></br>'), style)

    # Create a frame to make the text fit to the page, A4 format is used by default
    frame = Frame(0, 0, 21*cm, 29.7*cm, leftPadding=cm, bottomPadding=cm, rightPadding=cm, topPadding=cm,)
    # Add different parts of the story
    frame.addFromList(story, canvas)

    canvas.save()