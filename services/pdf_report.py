from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_pdf(transcribed_text):

    filename = "Voice_Analysis_Report.pdf"

    c = canvas.Canvas(filename, pagesize=letter)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, 750, "Voice Based Concept Understanding Analyzer")

    c.setFont("Helvetica", 12)
    c.drawString(50, 720, f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")

    c.drawString(50, 690, "Transcribed Text:")

    text = c.beginText(50, 670)
    text.setFont("Helvetica", 12)

    for line in transcribed_text.split("\n"):
        text.textLine(line)

    c.drawText(text)

    c.save()

    return filename
