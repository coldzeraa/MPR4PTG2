from myapi.db.ExaminationService import ExaminationService
from django.http import HttpResponse
from myapi.db.PatientService import PatientService
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from backend.settings import BASE_DIR
from myapi.export.ImageCreator import ImageCreator
import os
import io
import markdown

image_path = os.path.join(BASE_DIR, 'myapi', 'images', 'eye.png')
ishihara_path = "/ishihara_images/"


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
    def generate_ishihara_report(examination, patient):
        """
        Generates the Ishihara test report in HTML/Markdown format for the examination.

        :param examination: The examination object
        :param patient: The patient object
        :return: The markdown formatted content
        """

        def generate_image_paths():
            img_paths = [[], [], [], [], [], []]
            pictures_per_row = 2

            for row_idx in range(len(img_paths)):
                for img_idx in range(pictures_per_row):
                    img_paths[row_idx].append(f"image-{row_idx * pictures_per_row + (img_idx + 1)}.png")
            return img_paths

        def generate_table_row(row_paths):
            return " | | ".join(
                [f'<div style="text-align:center;"><img src="{ishihara_path}{path}" style="width:100px;"></div>' for
                 path in row_paths])

        current_datetime = examination.date
        result = '90%'

        header_content = (
            '<div style="display:flex; justify-content:space-between; align-items:center;">'
            f'<div style="flex:1; text-align:left;">'
            f'<img src="{image_path}" style="width:100px; margin:15px;">'
            '</div>'
            f'<div style="flex:1; text-align:right; font-size:14px; font-weight:bold;">'
            f'{current_datetime}'
            '</div>'
            '</div><br>'
        )

        footer_content = (
            '<div style="text-align:left; font-size:12px; margin-top:20px;">'
            '<strong>[ Wichtiger Hinweis ]</strong><br>'
            '<em>Bitte beachten Sie, dass OptiMate kein zertifiziertes Medizinprodukt ist und keinesfalls eine professionelle medizinische '
            'Diagnostik oder Therapie ersetzt. Konsultieren Sie bei medizinischen Anliegen stets einen qualifizierten Facharzt.</em>'
            '</div>'
        )

        img_paths = generate_image_paths()
        header = "| Bild | Ergebnis | Bild | Ergebnis |"
        separator = "|----------|----------|----------|----------|"
        rows = [generate_table_row(row) for row in img_paths]

        markdown_content = f"""
          {header_content}

          <div style="text-align:center;">
              <h1>Ishihara Ergebnis</h1>
              <h3>Gesamtresultat: {result}</h3>
          </div>

          ### Details:

          {header}
          {separator}
          {'\n'.join(rows)}

          {footer_content}
          """

        return markdown_content

    @staticmethod
    def create_ishihara_pdf(exID):
        """
        Generates a PDF report for the Ishihara examination with patient information, test results, and a disclaimer.

        :param exID: The ID of the examination
        :return: An HTTP response with the generated PDF as an attachment
        """
        examination = ExaminationService.get(id=exID)
        patient = PatientService.get(id=examination.pat.patID)

        markdown_content = PdfCreator.generate_ishihara_report(examination, patient)

        html_content = markdown.markdown(markdown_content)

        print("BLIB", html_content)

        return HttpResponse(html_content, content_type="text/html")