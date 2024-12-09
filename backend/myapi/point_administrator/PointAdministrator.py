import random
from myapi.db.PointService import PointService 


class PointAdministrator:
    
    @staticmethod
    def load_points():
        """
        Loads all points from the database that belong to the specified quadrant.

        :param quadrant: The quadrant for which the points should be loaded
        :return: A list of points from the specified quadrant
        """
        points = []
        
        for x in range(9, 97, 9):
            for y in range(9, 97, 9):
                points.append(PointService.get_point_by_x_and_y(x, y))
                        
        return points
        
