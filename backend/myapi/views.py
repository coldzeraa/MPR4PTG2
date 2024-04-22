from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapi.cruds import crud_patient

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        
        # get data from request
        first_name = request.data.get('firstName')
        last_name = request.data.get('lastName')
        email = request.data.get('email')
        
        # save patient in database
        crud_patient.create_patient(first_name, last_name, email)
        
        # return a success message
        return JsonResponse({'message': 'Login successful'}, status=200)
    else:
        
        # return a failed message
        return JsonResponse({'error': 'Invalid request method'}, status=405)

