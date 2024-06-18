from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapi.cruds import crud_patient
from myapi.db.PointResultService import PointResultService
from myapi.db.PointService import PointService
from myapi.db.PatientService import PatientService
from myapi.db.ExaminationService import ExaminationService
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from myapi.model.Point import Point
from myapi.model.Examination import Examination
from myapi.model.Patient import Patient
import datetime
from myapi.point_administrator.PointAdministrator import PointAdministrator
from myapi.export.email import send_email
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
from reportlab.lib.utils import ImageReader
import os
from backend.settings import BASE_DIR


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        # Get data from request
        first_name = str(request.data.get('firstName'))
        last_name = str(request.data.get('lastName'))
        email = str(request.data.get('email'))
        
        # Check if first_name, last_name and email is empty and save dummy in database
        if (not first_name and not last_name and not email):
            pat = PatientService.store()
            return JsonResponse({'message': 'SUCCESS', 'patientID': pat.patID}, status=200)
        
        # Check for invalid names
        if (not first_name.isalpha() or not last_name.isalpha()):
            return JsonResponse({"message": "INVALID_NAMES"})
        
        # Check if both names are entered
        if (not first_name and last_name) or (first_name and not last_name):
            return JsonResponse({"message": "NOT_BOTH_NAMES"})
    
        # Validate email
        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({"message": "NOT_AN_EMAIL"})
        
        # Save patient in database
        pat = PatientService.store(first_name, last_name, email)

        # Return a success message
        return JsonResponse({'message': 'SUCCESS', 'patientID': pat.patID}, status=200)
    else:
        
        # Return a failed message
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def emailing(request):
    print('I am in views.emailing')
    if request.method == 'POST':
        # Get data from request
        first_name = str(request.data.get('firstName'))
        last_name = str(request.data.get('lastName'))
        email_in = str(request.data.get('email'))
        pdf_base64 = str(request.data.get('pdfBase64'))

        email_instance = send_email(first_name, last_name, email_in, pdf_base64)
        email_instance.send_email()

        return JsonResponse({'message': 'SUCCESS'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def perimetry(request):
    if request.method == 'POST':
        x = request.data.get('x')
        y = request.data.get('y')
        exID = request.data.get('exID')
        result = request.data.get('result')
        id = 100 * x + y
        p = PointService.get(id)
        ex = ExaminationService.get(exID)

        PointResultService.store(result, p, ex)
        return JsonResponse({'message': 'SUCCESS'}, status=200)

@api_view(['GET'])
def get_points(request):
    
    # Raw list for points
    points = []
    
    print("get_points")
    # Request method
    if request.method == "GET":
        # Every quadrant
        for quadrant in range(1, 5):
            
            # Get all points of quadrant
            currentPoints = PointAdministrator.loadPoints(quadrant)
            # Get uniformly distributed indices
            pointIndices = PointAdministrator.getUniformedList(currentPoints)

            # Add points to point list
            points.extend([currentPoints[i] for i in pointIndices])
    
    # Send point list to frontend as json
    return JsonResponse({'points': [{'x': p.x, 'y': p.y} for p in points]}, status=200)

@api_view(['POST'])
def examination(request):
    if request.method == 'POST':
        patID = request.data.get("patID")
        pat = PatientService.get(patID)
        ex = ExaminationService.store(pat, datetime.datetime.today())
    return JsonResponse({'exID': ex.exID}, status=200)

@api_view(['GET'])
def get_pdf(request):
    if request.method == 'GET':
        
        # Extract examinationID from URL Parameter
        exID = request.GET.get('id', '')
        
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
        text = "OptiMate- Testergebnis"
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
        p.setFont("Helvetica", 12)
        p.drawString(70, 620, f"Patient: {patient.firstName} {patient.lastName}")
        
        # Results
        p.setFont("Helvetica", 11)
        p.drawString(70, 550, "Testergebnis: ")
        
        # Testresult
        image_path = os.path.join(BASE_DIR, 'myapi', 'images', 'david.png')
        img = ImageReader(image_path)
        p.drawImage(img, 110, 200, width=400, height=300)
        
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