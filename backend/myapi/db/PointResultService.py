from django.db.models import AutoField
from myapi.cruds import crud_point_result


class PointResultService:
    @staticmethod    
    def get_all():
        return crud_point_result.get_all_point_result()
    
    @staticmethod
    def store(seen: bool, pID: int, exID: int):
        return crud_point_result.create_point_result(seen, pID, exID)
    
    @staticmethod
    def get(id:AutoField):
        return crud_point_result.get_point_result_by_id(id)

    @staticmethod
    def update(resID: AutoField, seen: bool, pID: AutoField,  exID: AutoField):
        return crud_point_result.update_point_result(resID, seen, pID, exID)

    @staticmethod
    def delete(pID: AutoField):
        return crud_point_result.delete_point_result(pID)

    