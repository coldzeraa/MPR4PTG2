
from django.db.models import AutoField
from myapi.cruds import crud_patient
from myapi.db import Service

class PatientService():
    
    @property
    @staticmethod    
    def get_all():
        return crud_patient.get_all_patients()
    
    @staticmethod
    def store(firstName: str = "", lastName: str = "", email: str = ""):
        crud_patient.create_patient(firstName, lastName, email)
    
    @staticmethod
    def get(id:AutoField):
        return crud_patient.get_patient_by_id(id)

    @staticmethod
    def update(patID: AutoField, firstName: str, lastName: str):
        crud_patient.update_patient(patID, firstName, lastName)

    @staticmethod
    def delete(pID: AutoField):
        crud_patient.delete_patient(pID)

    