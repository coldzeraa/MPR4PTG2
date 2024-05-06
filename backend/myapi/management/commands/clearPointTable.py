from django.core.management.base import BaseCommand
from myapi.models import Point


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        Point.objects.all().delete()