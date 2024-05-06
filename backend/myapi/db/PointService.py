
import Service
from django.db.models import AutoField
from myapi.cruds import crud_point
from myapi.db import Service


class PointService():
    @property
    @staticmethod
    def get_all():
        return crud_point.get_all_points()
    
    @staticmethod
    def store(x: int, y: int, q: int):
        crud_point.create_point(x, y, q)
    
    @staticmethod
    def get(id:AutoField):
        return crud_point.get_point_by_id(id)

    @staticmethod
    def update(pID: AutoField, x: int, y: int, quadrant: int):
        crud_point.update_point(pID, x, y, quadrant)

    @staticmethod
    def delete(pID: AutoField):
        crud_point.delete_point(pID)

    