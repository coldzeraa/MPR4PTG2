from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapi.db.PatientService import PatientService
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        
        # Get data from request
        first_name = str(request.data.get('firstName'))
        last_name = str(request.data.get('lastName'))
        email = str(request.data.get('email'))
        
        # Check if first_name, last_name and email is empty and save dummy in database
        if (not first_name and not last_name and not email):
            PatientService.store()
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
        PatientService.store(first_name, last_name, email)
        
        # Return a success message
        return JsonResponse({'message': 'SUCCESS'}, status=200)
    else:
        
        # Return a failed message
        return JsonResponse({'error': 'Invalid request method'}, status=405)

