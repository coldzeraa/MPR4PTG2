from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view
from myapi.db.ResultPerimetryService import ResultPerimetryService
from myapi.db.PointService import PointService
from myapi.db.PatientService import PatientService
from myapi.db.ExaminationService import ExaminationService
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from datetime import datetime, timezone
from myapi.point_administrator.PointAdministrator import PointAdministrator
from myapi.export.EmailSender import EmailSender
from myapi.export.PdfCreator import PdfCreator
from myapi.models import Patient
import bcrypt


@api_view(['POST'])
def login(request):
    """
    Handles the login process for patients by validating and saving the provided information.

    :param request: The HTTP request object containing patient data (first name, last name, email)
    :return: A JsonResponse with a success message and patientID if successful, or an error message otherwise
    """
    if request.method == 'POST':
        # Get data from request
        email = str(request.data.get('email'))
        password = str(request.data.get('password'))

        # Search patient by email
        pat = PatientService.get_by_email(email)
        
        # Check if patient was found
        if not pat:
            return JsonResponse({'message': 'NO_PATIENT_FOUND'}, status=200)

        # Check if password is correct
        if bcrypt.checkpw(password.encode('utf-8'), pat.password.encode('utf-8')):
            return JsonResponse({'message': 'SUCCESS', 'patientID': pat.patID}, status=200)
        # Case password is incorrect
        else:
            return JsonResponse({'message': 'WRONG_PASSWORD'}, status=200)

    else:
        # Return a failed message
        return JsonResponse({'error': 'INVALID_REQUEST_METHOD'}, status=405)

@api_view(['POST'])
def emailing(request):
    """
    Handles the process of sending an email with a PDF attachment.

    :param request: The HTTP request object containing data (first name, last name, email, pdfBase64)
    :return: A JsonResponse with a success message if the email is sent, or an error message if the request method is invalid
    """
    
    if request.method == 'POST':
        # Get data from request
        first_name = str(request.data.get('firstName'))
        last_name = str(request.data.get('lastName'))
        email_in = str(request.data.get('email'))
        pdf_base64 = str(request.data.get('pdfBase64'))

        email_instance = EmailSender(first_name, last_name, email_in, pdf_base64)
        email_instance.send_email()

        return JsonResponse({'message': 'SUCCESS'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def perimetry(request):
    """
    Handles the process of storing perimetry results, associating them with a specific point and examination.

    :param request: The HTTP request object containing the x and y coordinates, examination ID (exID), and result
    :return: A JsonResponse with a success message if the result is stored successfully, or an error message if the request method is invalid
    """
    if request.method == 'POST':
        x = request.data.get('x')
        y = request.data.get('y')
        exID = request.data.get('exID')
        result = request.data.get('result')
        id = 100 * x + y
        p = PointService.get(id)
        ex = ExaminationService.get(exID)

        ResultPerimetryService.store(result, p, ex)
        return JsonResponse({'message': 'SUCCESS'}, status=200)

@api_view(['GET'])
def get_points(request):
    """
    Retrieves a uniformly distributed list of points from all quadrants and returns them as a JSON response.

    :param request: The HTTP request object
    :return: A JsonResponse containing a list of points with their x and y coordinates
    """
    
    # Raw list for points
    points = []
    
    print("get_points")
    # Request method
    if request.method == "GET":
        # Every quadrant
        for quadrant in range(1, 5):
            
            # Get all points of quadrant
            currentPoints = PointAdministrator.load_points(quadrant)
            # Get uniformly distributed indices
            pointIndices = PointAdministrator.get_uniformed_list(currentPoints)

            # Add points to point list
            points.extend([currentPoints[i] for i in pointIndices])
    
    # Send point list to frontend as json
    return JsonResponse({'points': [{'x': p.x, 'y': p.y} for p in points]}, status=200)

@api_view(['POST'])
def examination(request):
    """
    Handles the creation of a new examination by associating it with a patient and storing it in the database.

    :param request: The HTTP request object containing the patient ID (patID)
    :return: A JsonResponse containing the examination ID (exID) of the newly created examination
    """

    if request.method == 'POST':
        patID = request.data.get("patID")
        pat = PatientService.get(patID)
        type = 'P'
        ex = ExaminationService.store(pat, type, datetime.now(timezone.utc))
    return JsonResponse({'exID': ex.exID}, status=200)

@api_view(['GET'])
def get_pdf(request):
    """
    Handles the process of generating and returning a PDF file for the specified examination ID.

    :param request: The HTTP request object containing the examination ID (id) as a query parameter
    :return: A PDF response generated by the PdfCreator, or an error message if no ID is provided
    """
    if request.method == 'GET':
        
        # Call PDF creator with current exID
        return PdfCreator.createPDF(request.GET.get('id', ''))

@api_view(['GET'])
def get_patient_info(request):
    if request.method == 'GET':
        # Fetch patient info based on patient_id
        patient = PatientService.get(request.GET.get('patientID', ''))
        data = {
            "first_name": patient.firstName,
            "last_name": patient.lastName,
            "email": patient.email
        }
        return JsonResponse(data)

@api_view(['GET'])
def get_examinations(request):
    # Fetch examination records for a given patient
    examinations = ExaminationService.get_by_patient(request.GET.get('patientID'))
    data = {
        "examinations": [
            {
                "date_time": exam.date,
                "type": exam.type,
                "exID": exam.exID
            }
            for exam in examinations
        ]
    }
    print(data)
    return JsonResponse(data)

@api_view(['POST'])
def registry(request):
    """
    Handles the login process for patients by validating and saving the provided information.

    :param request: The HTTP request object containing patient data (first name, last name, email, password)
    :return: A JsonResponse with a success message and patientID if successful, or an error message otherwise
    """
    if request.method == 'POST':
        # Get data from request
        first_name = str(request.data.get('firstName'))
        last_name = str(request.data.get('lastName'))
        email = str(request.data.get('email'))
        password = str(request.data.get('password'))
        
        # Check if there is already a patient with this email
        if PatientService.get_by_email(email):
            return JsonResponse({"message": "PATIENT_ALREADY_EXISTS"})
        
        # Check for invalid names
        if (not first_name.isalpha() or not last_name.isalpha()):
            return JsonResponse({"message": "INVALID_NAMES"})
        
        # Validate email
        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({"message": "NOT_AN_EMAIL"})
        
        # Use bcrypt to hash password
        hashedPassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        # Save patient in database
        pat = PatientService.store(first_name, last_name, email, hashedPassword)

        # Return a success message
        return JsonResponse({'message': 'SUCCESS', 'patientID': pat.patID}, status=200)
    else:
        # Return a failed message
        return JsonResponse({'error': 'Invalid request method'}, status=405)@api_view(['GET'])
def get_patient_info(request):
    if request.method == 'GET':
        # Fetch patient info based on patient_id
        patient = PatientService.get(request.GET.get('patientID', ''))
        data = {
            "first_name": patient.firstName,
            "last_name": patient.lastName,
            "email": patient.email
        }
        return JsonResponse(data)

@api_view(['GET'])
def get_examinations(request):
    # Fetch examination records for a given patient
    examinations = ExaminationService.get_by_patient(request.GET.get('patientID'))
    data = {
        "examinations": [
            {
                "date_time": exam.date,
                "type": exam.type,
                "exID": exam.exID
            }
            for exam in examinations
        ]
    }
    print(data)
    return JsonResponse(data)