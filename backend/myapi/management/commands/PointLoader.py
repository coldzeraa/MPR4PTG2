from typing import List
from myapi.db.PointService import PointService
from django.core.management.base import BaseCommand
from myapi.model.Point import Point
from django.http import JsonResponse





class Command(BaseCommand):

    points = []

    def handle(self, *args, **options):
        query_set = PointService.get_all()
        self.points = [point for point in query_set]
        
        print(self.points)
        


