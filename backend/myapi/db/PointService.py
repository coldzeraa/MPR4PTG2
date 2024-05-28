
from django.db.models import AutoField
from myapi.cruds import crud_point
from myapi.model.Point import Point


class PointService:
    @staticmethod
    def get_all():
        return crud_point.get_all_points()
    
    @staticmethod
    def get_points_by_quadrant(quadrant: int):
        return crud_point.get_points_by_quadrant(quadrant)
    
    @staticmethod
    def store_by_parameters(x: int, y: int, q: int):
        return crud_point.create_point(x, y, q)
    
    @staticmethod
    def store(p: Point):
        x = p.get_x()
        y = p.get_y()
        q = p.get_quadrant()
        return PointService.store_by_parameters(x, y, q)
    
    @staticmethod
    def get(id: int):
        return crud_point.get_point_by_id(id)

    @staticmethod
    def update(pID: int, x: int, y: int, quadrant: int):
        return crud_point.update_point(pID, x, y, quadrant)

    @staticmethod
    def delete(pID: int):
        return crud_point.delete_point(pID)
