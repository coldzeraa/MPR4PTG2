import datetime
from django.db.models import AutoField
from backend.myapi.cruds import crud_examination


class ExaminationService:
    @staticmethod    
    def get_all():
        return crud_examination.get_all_examinations()
    
    @staticmethod
    def store(patID: AutoField, exDate = datetime.date.today()):
        crud_examination.create_examination(exDate, patID)
    
    @staticmethod
    def get(id:AutoField):
        return crud_examination.get_examination_by_id(id)

    @staticmethod
    def update(patID: AutoField, firstName: str, lastName: str):
        crud_examination.update_examination(patID, firstName, lastName)

    @staticmethod
    def delete(pID: AutoField):
        crud_examination.delete_examination(pID)

    