from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view
from myapi.db.PointResultService import PointResultService
from myapi.db.PointService import PointService
from myapi.db.PatientService import PatientService
from myapi.db.ExaminationService import ExaminationService
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import datetime
from myapi.point_administrator.PointAdministrator import PointAdministrator
from myapi.export.email import send_email
from myapi.export.pdfCreator import PdfCreator


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
        
        # Call PDF creator with current exID
        return PdfCreator.createPDF(request.GET.get('id', ''))

