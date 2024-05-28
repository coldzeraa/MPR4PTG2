from django.http import JsonResponse
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

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        
        # Get data from request
        first_name = str(request.data.get('firstName'))
        last_name = str(request.data.get('lastName'))
        email = str(request.data.get('email'))
        
        # Check if first_name, last_name and email is empty and save dummy in database
        if (not first_name and not last_name and not email):
            crud_patient.create_patient()
            return JsonResponse({'message': 'SUCCESS'}, status=200)
        
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
        crud_patient.create_patient(first_name, last_name, email)
        
        # Return a success message
        return JsonResponse({'message': 'SUCCESS'}, status=200)
    else:
        
        # Return a failed message
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def perimetry(request):
    if request.method == 'POST':
        
        x = request.data.get('x')
        y = request.data.get('y')
        result = request.data.get('result')
        print(result, x, y)
        p = PointService.get(100*x+y)
        pat = PatientService.store("Alex", "Denk")
        e = ExaminationService.store(pat, datetime.datetime.today())
        PointResultService.store(result, p, e)
        return JsonResponse({'message': 'SUCCESS'}, status=200)

