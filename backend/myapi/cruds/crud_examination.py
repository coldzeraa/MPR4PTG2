from datetime import datetime

from myapi.models import Examination, Patient
from django.db.models import AutoField
from myapi.db.PatientService import PatientService


def create_examination(exDate: datetime, pat: Patient, type: str):
    """
        Create a new Examination object

        :param exDate: date of examination
        :param patID: patient ID
        :param type: type of examination
        :return: new examination
       """
    return Examination.objects.create(date=exDate, pat=pat, type=type)

def get_all_examinations():
    """
       Get all Examinations
    """
    return Examination.objects.all()

def get_examination_by_id(exID: AutoField):
    """
       Get Examination by given ID

       :param exID: examination ID
       :return: Examination Object
    """
    return Examination.objects.get(exID=exID)

def update_examination(exID: AutoField, exDate: datetime, pat: Patient, type: str):
    """
          Update Examination

          :param exID: id of examination
          :param exDate: date of examination
          :param type: type of examination
          :return: Examination Object
       """
    examination = Examination.objects.get(exID=exID)
    examination.date = exDate
    examination.pat = pat
    examination.type = type
    examination.save()
    return examination

def delete_examination(exID: AutoField):
    """
          Delete Examination

          :param exID: id of examination
    """
    examination = Examination.objects.get(exID=exID)
    examination.delete()

def get_examinations_by_patient(patient_id: AutoField):
    """
          Get Examinations by Patients.

          :param patient_id: id of patient
    """
    pat = PatientService.get(patient_id)
    examinations = Examination.objects.filter(pat=pat)
    return examinations
