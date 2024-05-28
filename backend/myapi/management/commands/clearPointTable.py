from django.core.management.base import BaseCommand
from myapi.models import Point1
from django.db import connection



class Command(BaseCommand):
    
    def handle(self, *args, **options):
        
        # Delete every entry in table
        Point1.objects.all().delete()
        
        # Manually set pID to 1 that the new values start with id 1
        with connection.cursor() as cursor:
            cursor.execute("SELECT setval(pg_get_serial_sequence('myapi_point', 'pID'), 1, false);")