import random
from myapi.db.PointService import PointService 


class PointAdministrator:
    
    @staticmethod
    def load_points(quadrant: int):
        """
        Loads all points from the database that belong to the specified quadrant.

        :param quadrant: The quadrant for which the points should be loaded
        :return: A list of points from the specified quadrant
        """
        # Get every point from the database for the given quadrant
        query_set = PointService.get_points_by_quadrant(quadrant)
        # Return the list of points
        return [point for point in query_set]
    
    @staticmethod
    def get_uniformed_list(points: list):
        """
        Generates a list of randomly selected point indices from the given list of points.
        A fixed number of points per quadrant are selected uniformly.

        :param points: A list of points to select from
        :return: A list of randomly selected indices from the points list
        """
        # Predefined number of points to select per quadrant
        NUMBER_POINTS_PER_QUADRANT = 19
        # Get NUMBER_POINTS_PER_QUADRANT uniformly distributed indices from the points list
        return [int(random.uniform(0, len(points))) for _ in range(NUMBER_POINTS_PER_QUADRANT)] 
