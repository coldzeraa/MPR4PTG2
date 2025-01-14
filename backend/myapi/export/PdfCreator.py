from myapi.db.ExaminationService import ExaminationService
from django.http import HttpResponse
from myapi.db.PatientService import PatientService
from myapi.db.ResultIshiharaService import ResultIshiharaService
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from backend.settings import BASE_DIR
from myapi.export.ImageCreator import ImageCreator
import os
import io

image_path = os.path.join(BASE_DIR, 'myapi', 'images', 'eye.png')
ishihara_path = os.path.abspath(os.path.join(BASE_DIR, '..', 'frontend', 'public', 'ishihara_images'))

class PdfCreator:

    @staticmethod
    def create_perimetry_pdf(exID):
        """
            Generates a PDF report for an examination with patient information, test results, and a disclaimer.

            :param exID: The ID of the examination
            :return: An HTTP response with the generated PDF as an attachment
        """

        examination = ExaminationService.get(id=exID)
        patient = PatientService.get(id=examination.pat.patID)

        buffer = io.BytesIO()

        p = canvas.Canvas(buffer, pagesize=letter)

        # title
        p.setTitle("Optimate Testergebnis")

        # header
        text = "OptiMate Testergebnis"
        text_width = p.stringWidth(text, "Helvetica-Bold", 16)
        x = (letter[0] - text_width) / 2
        p.setFont("Helvetica-Bold", 16)
        p.drawString(x, 670, text)

        # image
        img = ImageReader(image_path)
        p.drawImage(img, 50, 710, width=100, height=50)

        # date
        p.setFont('Helvetica', 10)
        formatted_date = examination.date.strftime("%d.%m.%Y %H:%M")
        p.drawString(480, 740, formatted_date)

        # patient info
        if (patient.firstName is not None and patient.lastName is not None):
            p.setFont("Helvetica", 12)
            p.drawString(70, 620, f"Patient: {patient.firstName} {patient.lastName}")

        # results
        p.setFont("Helvetica", 11)
        p.drawString(70, 550, "Testergebnis: ")

        # test result
        img = ImageReader(ImageCreator.create_image(exID))
        p.drawImage(img, 105, 250, width=408, height=204)

        p.drawString(105, 460, "Linkes Auge")
        p.drawString(313, 460, "Rechtes Auge")

        # hint
        p.setFont("Helvetica-Bold", 8)
        p.drawString(70, 65, "[Wichtiger Hinweis]")

        # text of hint
        p.setFont("Helvetica-Oblique", 8)
        text = """Bitte beachten Sie, dass OptiMate kein zertifiziertes Medizinprodukt ist und keinesfalls eine professionelle 
                    medizinische Diagnostik oder Therapie ersetzt. Konsultieren Sie bei medizinischen Anliegen stets einen qualifizierten 
                    Facharzt."""

        # text position
        x = 70
        y = 50
        width = 500

        # info text
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

        # print lines
        for line in lines:
            p.drawString(x, y, line)
            y -= 14

        p.showPage()

        p.save()

        # set curser to beginning
        buffer.seek(0)

        # send response
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="medical_report.pdf"'

        return response

    @staticmethod
    def get_ishihara_images():
        image_files = []

        for filename in os.listdir(ishihara_path):
            image_files.append(os.path.join(ishihara_path, filename))

        return image_files

    @staticmethod
    def create_ishihara_pdf(exID):
        """
            Generates a PDF report for an examination with patient information, test results, and a disclaimer.

            :param exID: The ID of the examination
            :return: An HTTP response with the generated PDF as an attachment
        """

        examination = ExaminationService.get(id=exID)
        patient = PatientService.get(id=examination.pat.patID)
        ex_results = ResultIshiharaService.getByExID(exID)

        buffer = io.BytesIO()

        p = canvas.Canvas(buffer, pagesize=letter)

        # title
        p.setTitle("Optimate Testergebnis")

        # header
        text = "OptiMate Testergebnis"
        text_width = p.stringWidth(text, "Helvetica-Bold", 16)
        x = (letter[0] - text_width) / 2
        p.setFont("Helvetica-Bold", 16)
        p.drawString(x, 670, text)

        # image
        img = ImageReader(image_path)
        p.drawImage(img, 50, 710, width=100, height=50)

        # date
        p.setFont('Helvetica', 10)
        formatted_date = examination.date.strftime("%d.%m.%Y %H:%M")
        p.drawString(480, 740, formatted_date)

        results = [ r for r in ex_results if r.recognized ]
        score = int(round(len(results)/len(ex_results), 2) * 100)

        # patient info
        if (patient.firstName is not None and patient.lastName is not None):
            p.setFont("Helvetica", 12)
            p.drawString(70, 620, f"Patient: {patient.firstName} {patient.lastName}")
            p.drawString(70, 600, f"Ergebnis: {score}%")

        # hint
        p.setFont("Helvetica-Bold", 8)
        p.drawString(70, 65, "[Wichtiger Hinweis]")

        # text of hint
        p.setFont("Helvetica-Oblique", 8)
        text = """Bitte beachten Sie, dass OptiMate kein zertifiziertes Medizinprodukt ist und keinesfalls eine professionelle 
                    medizinische Diagnostik oder Therapie ersetzt. Konsultieren Sie bei medizinischen Anliegen stets einen qualifizierten 
                    Facharzt."""

        # text position
        x = 70
        y = 50
        width = 500

        # info text
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

        # print lines
        for line in lines:
            p.drawString(x, y, line)
            y -= 14

        x_start = 55
        y_start = 610

        x = x_start
        y = y_start

        text_img_offset = 107

        p.setFont("Helvetica-Bold", 8)

        ishihara_images = PdfCreator.get_ishihara_images()
        for idx in range(len(ishihara_images)):
            if not idx % 3:
                y -= 125
                x = x_start

            img = ImageReader(ishihara_images[idx])
            p.drawImage(img, x, y, width=100, height=100)

            p.drawString(x + text_img_offset, y + 50,
                         'erkannt' if ex_results[idx].recognized else 'nicht erkannt')

            x += 175

        p.showPage()

        p.save()

        # set curser to beginning
        buffer.seek(0)

        # send response
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="medical_report.pdf"'

        return response