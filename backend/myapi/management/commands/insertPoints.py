from myapi.db.PointService import PointService
from django.core.management.base import BaseCommand
import random


class Command(BaseCommand):
    
    # Check quadrant of point
    def getQuadrant(self, x, y):
        if x < 48 and y >= 48:
            return 1
        elif x >= 48 and y >= 48:
            return 2
        elif x < 48 and y < 48:
            return 3
        elif x >= 48 and y < 48:
            return 4
        
    # Override handle function -> to call script with manage.py
    def handle(self, *args, **options):
        
        # Point DAO
        ps = PointService()  

        # Number of points
        numPoints = 76

        # Quadrants [[1], [2], [3], [4]]
        quadrants = [[(0, 47), (48, 97)], [(48, 79), (48, 97)], [(0, 47), (0, 47)], [(48, 79), (0, 47)]]
        
        # Calculate number of points in every quadrant
        numPointsQuadrant = (int)(numPoints / 4)
        
        for quadrant in quadrants:
            
            for _ in range(numPointsQuadrant):
            
                # Get range of current quadrant
                xRange = quadrant[0]
                yRange = quadrant[1]
                
                # Gete random number in current quadrant
                x = random.randint(*xRange)
                y = random.randint(*yRange)
                
                # Identify quadrant
                q = self.getQuadrant(x, y)
                
                # Store point in database
                ps.store(x, y, q)
            