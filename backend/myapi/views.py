from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapi.cruds import crud_patient
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from myapi.point_administrator.PointAdministrator import PointAdministrator
from myapi.db.PointService import PointService


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


@api_view(['GET'])
def getPoints(request):
    
    if request.method == 'GET':
        
        # Initialize empty list
        selectedPoints = []
        
        # Iterate quadrants
        for q in range (1, 5):

            # Get points of current quadrant from loader
            points = PointAdministrator.loadPoints(q)
            
            # Get all points from database
            query = PointService.get_all()
            
            # Convert to list
            query = [point for point in query]
    
            # Get 19 uniformed indices 
            uniformedList = PointAdministrator.getUniformedList(points)
            
            # Add uniformed points to dict
            for i in uniformedList:
                selectedPoints.append(points[i])                                        
                    
        # Return JSON with all points
        return Response({'message': [
            [{'point': str(point)} for point in selectedPoints]
        ]})
        
    else:
        raise RuntimeError
    
    

    