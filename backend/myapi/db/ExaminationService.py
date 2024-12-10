from datetime import datetime
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
    def store(patID: AutoField, type: str, exDate = datetime):
        """
            Store examination in database

            :param patID: ID of patient
            :param exDate: date of examination
            :param type: type of examination
            :return: new examination
        """
        return crud_examination.create_examination(exDate, patID, type)
    
    @staticmethod
    def get(id:AutoField):
        """
            Get examination by given ID

            :param ID: ID of examination
            :return: Examination Object
        """
        return crud_examination.get_examination_by_id(id)

    @staticmethod
    def update(patID: AutoField, firstName: str, lastName: str, type: str):
        """
            Update examination

            :param patID: ID of patient
            :param firstName: new first name
            :param lastName: new last name
            :param type: new type
            :return: updated Examination Object
        """
        return crud_examination.update_examination(patID, firstName, lastName, type)

    @staticmethod
    def delete(exID: AutoField):
        """
            Delete examination

            :param exID: ID of examination
        """
        return crud_examination.delete_examination(exID=exID)

    def get_by_patient(pID: AutoField):
        """
            Get Examination by Patient ID.

            :param pID: ID of patient
        """
        return crud_examination.get_examinations_by_patient(pID)