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
        
        for x in range(0, 98):
            
            for y in range(0, 98):
                
                # Identify quadrant
                q = self.getQuadrant(x, y)
                
                # Store point in database
                ps.store(x, y, q)
            