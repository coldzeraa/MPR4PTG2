from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        first_name = request.data.get('firstName')
        last_name = request.data.get('lastName')
        email = request.data.get('email')

        return JsonResponse({'message': 'Login successful'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

