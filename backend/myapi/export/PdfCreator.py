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
import json

image_path = os.path.join(BASE_DIR, 'myapi', 'images', 'eye.png')
ishihara_path = os.path.abspath(os.path.join(BASE_DIR, '..', 'frontend', 'public', 'ishihara_images'))
ishihara_results_path = os.path.join(BASE_DIR, 'data', 'ishihara_results.json')

class PdfCreator:
    @staticmethod
    def draw_header(p, examination, title="OptiMate Testergebnis"):
        """
        Draws the common header section for the PDF, including the title, logo, and date.
        """
        # title
        p.setTitle(title)
        text_width = p.stringWidth(title, "Helvetica-Bold", 16)
        x = (letter[0] - text_width) / 2
        p.setFont("Helvetica-Bold", 16)
        p.drawString(x, 670, title)

        # logo
        img = ImageReader(image_path)
        p.drawImage(img, 50, 710, width=100, height=50)

        # date
        p.setFont('Helvetica', 10)
        formatted_date = examination.date.strftime("%d.%m.%Y %H:%M")
        p.drawString(480, 740, formatted_date)

    @staticmethod
    def draw_patient_info(p, patient, additional_info=None):
        """
        Draws the patient information on the PDF.
        """
        if patient.firstName and patient.lastName:
            p.setFont("Helvetica", 12)
            p.drawString(70, 620, f"Patient: {patient.firstName} {patient.lastName}")
            if additional_info:
                for idx, info in enumerate(additional_info, start=1):
                    p.drawString(70, 620 - 20 * idx, info)

    @staticmethod
    def draw_hint(p):
        """
        Draws the common disclaimer or hint text at the bottom of the PDF.
        """
        # header
        p.setFont("Helvetica-Bold", 8)
        p.drawString(70, 65, "[Wichtiger Hinweis]")

        # text
        p.setFont("Helvetica-Oblique", 8)
        text = """Bitte beachten Sie, dass OptiMate kein zertifiziertes Medizinprodukt ist und keinesfalls eine professionelle 
                    medizinische Diagnostik oder Therapie ersetzt. Konsultieren Sie bei medizinischen Anliegen stets einen qualifizierten 
                    Facharzt."""

        x = 70
        y = 50
        width = 500

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

        for line in lines:
            p.drawString(x, y, line)
            y -= 14

    @staticmethod
    def create_perimetry_pdf(exID):
        """
        Generates a PDF report for a perimetry examination.
        """
        examination = ExaminationService.get(id=exID)
        patient = PatientService.get(id=examination.pat.patID)

        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)

        # common sections
        PdfCreator.draw_header(p, examination)
        PdfCreator.draw_patient_info(p, patient)
        PdfCreator.draw_hint(p)

        # perimetry specific sections
        p.setFont("Helvetica", 11)
        p.drawString(70, 550, "Testergebnis: ")

        # test result image
        img = ImageReader(ImageCreator.create_image(exID))
        p.drawImage(img, 105, 250, width=408, height=204)
        p.drawString(105, 460, "Linkes Auge")
        p.drawString(313, 460, "Rechtes Auge")

        p.showPage()
        p.save()

        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="medical_report.pdf"'
        return response

    @staticmethod
    def get_ishihara_images():
        image_files = []

        for filename in os.listdir(ishihara_path):
            image_files.append(os.path.join(ishihara_path, filename))

        image_files.sort(key=lambda x: int(x.split('image-')[1].replace(".png", "").strip()))

        return image_files

    @staticmethod
    def create_ishihara_pdf(exID):
        """
        Generates a PDF report for an Ishihara examination.
        """
        examination = ExaminationService.get(id=exID)
        patient = PatientService.get(id=examination.pat.patID)
        ex_results = ResultIshiharaService.getByExID(exID)

        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)

        # common sections
        PdfCreator.draw_header(p, examination)
        score = int(round(len([r for r in ex_results if r.recognized]) / len(ex_results), 2) * 100)
        PdfCreator.draw_patient_info(p, patient, additional_info=[f"Ergebnis: {score}%"])
        PdfCreator.draw_hint(p)

        # ishihara specific sections
        x_start = 55
        y_start = 610
        x = x_start
        y = y_start
        text_img_offset = 107

        p.setFont("Helvetica-Bold", 8)
        ishihara_images = PdfCreator.get_ishihara_images()

        with open(ishihara_results_path, 'r') as file:
            results_json = json.load(file)

        for idx in range(len(ishihara_images)):
            if not idx % 3:
                y -= 125
                x = x_start

            img = ImageReader(ishihara_images[idx])
            p.drawImage(img, x, y, width=100, height=100)
            solution_data = results_json['solutions'][idx]
            correct_number = solution_data[str(idx + 1)]['number']

            p.drawString(x + text_img_offset, y + 55, f"Lösung: {correct_number}")
            p.drawString(x + text_img_offset, y + 30,
                         'korrekt' if ex_results[idx].recognized else 'nicht korrekt')

            x += 175

        p.showPage()
        p.save()

        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="medical_report.pdf"'
        return response
