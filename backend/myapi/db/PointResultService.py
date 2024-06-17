from django.db.models import AutoField
from myapi.cruds import crud_point_result
from myapi.model.Point import Point
from myapi.model.Examination import Examination


class PointResultService:
    @staticmethod    
    def get_all():
        return crud_point_result.get_all_point_results()
    
    @staticmethod
    def store(seen: bool, p: Point, ex: Examination):
        return crud_point_result.create_point_result(seen, p, ex)
    
    @staticmethod
    def get(id:AutoField):
        return crud_point_result.get_point_result_by_id(id)

    @staticmethod
    def update(resID: AutoField, seen: bool, pID: AutoField,  exID: AutoField):
        return crud_point_result.update_point_result(resID, seen, pID, exID)

    @staticmethod
    def delete(pID: AutoField):
        return crud_point_result.delete_point_result(pID)

    