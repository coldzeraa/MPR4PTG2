from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapi.cruds import crud_patient
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        
        # get data from request
        first_name = str(request.data.get('firstName'))
        last_name = str(request.data.get('lastName'))
        email = str(request.data.get('email'))
        
        # TODO invalid names
        if (not first_name.isalpha() or not last_name.isalpha()):
            return JsonResponse({"message": "INVALID_NAMES"})
        
        # check if both names are entered
        if (not first_name and last_name) or (first_name and not last_name):
            return JsonResponse({"message": "NOT_BOTH_NAMES"})
    
        # validate email
        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({"message": "NOT_AN_EMAIL"})
        
        # save patient in database
        crud_patient.create_patient(first_name, last_name, email)
        
        # return a success message
        return JsonResponse({'message': 'SUCCESS'}, status=200)
    else:
        
        # return a failed message
        return JsonResponse({'error': 'Invalid request method'}, status=405)

