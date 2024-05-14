import random
from myapi.db.PointService import PointService 


class PointAdministrator:
    
    @staticmethod
    def loadPoints(quadrant: int):
        # Get every point from database
        query_set = PointService.get_points_by_quadrant(quadrant)
        # Return with list comprehension
        return [point for point in query_set]
    
    @staticmethod
    def getUniformedList(points: list):
        # Predefined value
        NUMBER_POINTS_PER_QUADRANT = 19
        # Get NUMBER_POINTS_PER_QUADRANT uniformly distributed indices from points list
        return [int(random.uniform(0, len(points))) for _ in range(NUMBER_POINTS_PER_QUADRANT)] 
        
        