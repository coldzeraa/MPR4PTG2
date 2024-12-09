from django.db.models import AutoField
from myapi.cruds import crud_ishihara_result
from myapi.model.Examination import Examination


class ResultIshiharaService:
    @staticmethod    
    def get_all():
        """
            Get all ishihara results from database

            :return: all ishihara results
        """
        return crud_ishihara_result.get_all_ishihara_results()
    
    @staticmethod
    def store(filename: str, recognized: bool, ex: Examination):
        """
            Store ishihara result in database

            :param filename: name of affected file
            :param recognized: specifies if image was recognized 
            :param ex: affected examination
            :return: new ishihara result
        """
        return crud_ishihara_result.create_ishihara_result(filename, recognized, ex)
    
    @staticmethod
    def get(id:AutoField):
        """
            Get ishihara result by given ID

            :param ID: ID of ishihara result
            :return: point ishihara Object
        """
        return crud_ishihara_result.get_ishihara_result_by_id(id)

    @staticmethod
    def update(resID: int, filename: str, recognized: bool,  exID: AutoField):
        """
            Update IshiharaResult

            :param resID: ID of IshiharaResult
            :param filename: name of affected file
            :param recognized: specifies if image was recognized 
            :param exID: id of affected examination
            :return: updated ishihara result Object
        """
        return crud_ishihara_result.update_ishihara_result(resID, filename, recognized, exID)

    @staticmethod
    def delete(resID: AutoField):
        """
            Delete ishihara result

            :param resID: ID of ishihara result
        """
        return crud_ishihara_result.delete_ishihara_result(resID)
    
    @staticmethod
    def getByExID(exID: AutoField):
        """
            Get ishihara results by examination id

            :param exID: ID of affected examination
        """
        return crud_ishihara_result.get_ishihara_result_by_exID(exID)
    