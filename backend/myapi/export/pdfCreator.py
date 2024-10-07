from django.http import HttpResponse
from myapi.db.ExaminationService import ExaminationService
from myapi.db.PatientService import PatientService
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
from reportlab.lib.utils import ImageReader
import os
from backend.settings import BASE_DIR
from myapi.export.imageCreator import ImageCreator

class PdfCreator:
    
    @staticmethod
    def createPDF(exID):
        
        # Get examination
        examination = ExaminationService.get(exID)
        
        # Get patient
        patient = PatientService.get(examination.pat.patID)
        
        buffer = io.BytesIO()
        
        # Create pdf
        p = canvas.Canvas(buffer, pagesize=letter)
        
        # Title
        p.setTitle("Optimate Testergebnis")
        
        # Headline
        text = "OptiMate Testergebnis"
        text_width = p.stringWidth(text, "Helvetica-Bold", 16)
        x = (letter[0] - text_width) / 2
        p.setFont("Helvetica-Bold", 16)
        p.drawString(x, 670, text)
        
        # Image
        image_path = os.path.join(BASE_DIR, 'myapi', 'images', 'eye.png')
        img = ImageReader(image_path)
        p.drawImage(img, 50, 710, width=100, height=50)
        
        # Date
        p.setFont('Helvetica', 10)
        p.drawString(500, 740, str(examination.date))
        
        # Patient information
        if (patient.firstName is not None and patient.lastName is not None):
            p.setFont("Helvetica", 12)
            p.drawString(70, 620, f"Patient: {patient.firstName} {patient.lastName}")
        
        # Results
        p.setFont("Helvetica", 11)
        p.drawString(70, 550, "Testergebnis: ")
        
        # Testresult
        img = ImageReader(ImageCreator.createImage(exID))
        p.drawImage(img, 105, 250, width=408, height=204)
        
        # Left eye, right eye
        p.drawString(105, 460, "Linkes Auge")
        p.drawString(313, 460, "Rechtes Auge")
        
        
        # Hint
        p.setFont("Helvetica-Bold", 8)
        p.drawString(70, 65, "[Wichtiger Hinweis]")

        # Text of hint
        p.setFont("Helvetica-Oblique", 8)
        text = """Bitte beachten Sie, dass OptiMate kein zertifiziertes Medizinprodukt ist und keinesfalls eine professionelle 
                    medizinische Diagnostik oder Therapie ersetzt. Konsultieren Sie bei medizinischen Anliegen stets einen qualifizierten 
                    Facharzt."""
                    
        
        # Position of text
        x = 70
        y = 50
        width = 500
        
        # Split information text
        lines = []
        words = text.split()
        line = ""
        for word in words:
            if p.stringWidth(line + " " + word) <= width:
                line += " " + word if line else word
            else:
                lines.append(line.lstrip())
                line = word
        lines.append(line.lstrip())
        
        # Print every line
        for line in lines:
            p.drawString(x, y, line)
            y -= 14
        
        p.showPage()
        
        p.save()
        
        # Set curser to beginning
        buffer.seek(0)
        
        # Http response
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="medical_report.pdf"'
        
        return response
        