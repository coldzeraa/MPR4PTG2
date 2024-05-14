from myapi.db.PointService import PointService 


class PointLoader:

    @staticmethod
    def loadPoints():
        # Get every point from database
        query_set = PointService.get_all()
        # Return with list comprehension
        return [point for point in query_set]