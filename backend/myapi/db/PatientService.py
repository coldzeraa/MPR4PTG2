from django.db.models import AutoField
from myapi.cruds import crud_patient


class PatientService:
    @staticmethod    
    def get_all():
        """
            Get all patients from database

            :return: all patients
        """
        return crud_patient.get_all_patients()
    
    @staticmethod
    def store(firstName: str = "", lastName: str = "", password: str = "", email: str = ""):
        """
            Store patient in database

            :param firstName: first name of patient
            :param lastName: last name of patient
            :param password: hashed password of patient
            :param email: email of patient
            :return: new patient
        """
        return crud_patient.create_patient(firstName, lastName, password, email)
    
    @staticmethod
    def get(id:AutoField):
        """
            Get patient by given ID

            :param ID: ID of patient
            :return: Patient Object
        """
        return crud_patient.get_patient_by_id(id)

    @staticmethod
    def update(patID: AutoField, firstName: str, lastName: str, password: str):
        """
            Update patient

            :param patID: ID of patient
            :param firstName: new first name
            :param lastName: new last name
            :param passeord: new hashed password
            :return: updated Patient Object
        """
        return crud_patient.update_patient(patID, firstName, lastName, password)

    @staticmethod
    def delete(pID: AutoField):
        """
            Delete patient

            :param pID: ID of patient
        """
        return crud_patient.delete_patient(pID)

    