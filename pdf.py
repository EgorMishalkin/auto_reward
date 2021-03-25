from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = io.BytesIO()
# Create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=letter)
can.setFont('Helvetica-Bold', 24)
can.drawString(10, 100, "Hello world")
can.showPage()
can.save()

# Move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# Read your existing PDF
existing_pdf = PdfFileReader(open("shablon_gramoty.pdf", "rb"))
output = PdfFileWriter()
# Add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# Finally, write "output" to a real file
outputStream = open("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()