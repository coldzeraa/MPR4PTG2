from myapi.db.PointService import PointService
from django.core.management.base import BaseCommand
import random


class Command(BaseCommand):
    
    # Check quadrant of point
    def getQuadrant(self, x, y):
        if x < 50 and y >= 50:
            return 1
        elif x >= 50 and y >= 50:
            return 2
        elif x < 50 and y < 50:
            return 3
        elif x >= 50 and y < 50:
            return 4
        
    # Override handle function -> to call script with manage.py
    def handle(self, *args, **options):
        
        # Point DAO
        ps = PointService()  

        num_points = 76

        # Quadrants
        yRanges = [(0, 50), (50, 100)]
        xRanges = [(0, 50), (50, 100)]
        
        for _ in range(num_points):
            
            xRange = random.choice(xRanges)
            yRange = random.choice(yRanges)
            
            x = random.randint(*xRange)
            y = random.randint(*yRange)
            
            q = self.getQuadrant(x, y)
            
            ps.store(x, y, q)
        