
from django.db.models import AutoField
from myapi.cruds import crud_point
from myapi.model.Point import Point


class PointService:
    @staticmethod
    def get_all():
        """
            Get all points from database

            :return: all points
        """
        return crud_point.get_all_points()
    
    @staticmethod
    def get_points_by_quadrant(quadrant: int):
        """
            Get all points from given quadrant

            :param quadrant: number of quadrant
            :return: all points of this quadrant
        """
        return crud_point.get_points_by_quadrant(quadrant)
    
    @staticmethod
    def get_point_by_x_and_y(x: int, y: int):
        return crud_point.get_point_by_x_and_y(x, y)
    
    @staticmethod
    def store_by_parameters(x: int, y: int, q: int):
        """
            Store point in database

            :param x: x coordinate
            :param y: y coordinate
            :param q: quadrant
            :return: new point object
        """
        return crud_point.create_point(x, y, q)
    
    @staticmethod
    def store(p: Point):
        """
            Store point in database

            :param p: point object
            :return: new point object
        """
        x = p.get_x()
        y = p.get_y()
        q = p.get_quadrant()
        return PointService.store_by_parameters(x, y, q)
    
    @staticmethod
    def get(id: int):
        """
            Get point by given ID

            :param ID: ID of point
            :return: point Object
        """
        return crud_point.get_point_by_id(id)

    @staticmethod
    def update(pID: int, x: int, y: int, quadrant: int):
        """
            Update point

            :param pID: ID of point
            :param x: x coordinate
            :param y: y coordinate
            :param quadrant: quadrant of point
            :return: updated point Object
        """
        return crud_point.update_point(pID, x, y, quadrant)

    @staticmethod
    def delete(pID: int):
        """
            Delete point

            :param pID: ID of point
        """
        return crud_point.delete_point(pID)