from django.db.models import AutoField
from myapi.cruds import crud_perimetry_result
from myapi.model.Point import Point
from myapi.model.Examination import Examination


class ResultPerimetryService:
    @staticmethod    
    def get_all():
        """
            Get all point results from database

            :return: all point results
        """
        return crud_perimetry_result.get_all_perimetry_results()
    
    @staticmethod
    def store(seen: bool, p: Point, ex: Examination):
        """
            Store point result in database

            :param seen: boolean if point was seen
            :param p: affected point
            :param ex: affected examination
            :return: new point result
        """
        return crud_perimetry_result.create_perimetry_result(seen, p, ex)
    
    @staticmethod
    def get(id:AutoField):
        """
            Get point result by given ID

            :param ID: ID of point result
            :return: point result Object
        """
        return crud_perimetry_result.get_perimetry_result_by_id(id)

    @staticmethod
    def update(resID: AutoField, seen: bool, pID: AutoField,  exID: AutoField):
        """
            Update patient

            :param resID: ID of point result
            :param seen: boolean if point was seen
            :param pID: id of affected point
            :param exID: id of affected examination
            :return: updated point result Object
        """
        return crud_perimetry_result.update_perimetry_result(resID, seen, pID, exID)

    @staticmethod
    def delete(pID: AutoField):
        """
            Delete point result

            :param pID: ID of point result
        """
        return crud_perimetry_result.delete_perimetry_result(pID)
    
    @staticmethod
    def getByExID(exID: AutoField):
        """
            Get point results by examination id

            :param exID: ID of affected examination
        """
        return crud_perimetry_result.get_perimetry_result_by_exID(exID)
    