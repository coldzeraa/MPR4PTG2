import datetime
from django.db.models import AutoField
from myapi.cruds import crud_examination


class ExaminationService:
    @staticmethod    
    def get_all():
        """
            Get all examinations from database

            :return: all examinations
        """
        return crud_examination.get_all_examinations()
    
    @staticmethod
    def store(patID: AutoField, exDate = datetime.date.today()):
        """
            Store examination in database

            :param patID: ID of patient
            :param exDate: date of examination
            :return: new examination
        """
        return crud_examination.create_examination(exDate, patID)
    
    @staticmethod
    def get(id:AutoField):
        """
            Get examination by given ID

            :param ID: ID of examination
            :return: Examination Object
        """
        return crud_examination.get_examination_by_id(id)

    @staticmethod
    def update(patID: AutoField, firstName: str, lastName: str):
        """
            Update examination

            :param patID: ID of patient
            :param firstName: new first name
            :param lastName: new last name
            :return: updated Examination Object
        """
        return crud_examination.update_examination(patID, firstName, lastName)

    @staticmethod
    def delete(pID: AutoField):
        """
            Delete examination

            :param patID: ID of patient
        """
        return crud_examination.delete_examination(pID)

    