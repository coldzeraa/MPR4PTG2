from datetime import date

from backend.myapi.models import Examination, Patient
from django.db.models import AutoField


def create_examination(exDate: date, patID: AutoField):
    """
        Create a new Examination object

        :param exDate: date of examination
        :param patID: patient ID
        :return: new examination
       """
    patient = Patient.objects.get(patID=patID)
    return Examination.objects.create(date=exDate, pat=patient)


def get_examination_by_id(exID: AutoField):
    """
       Get Examination by given ID

       :param exID: examination ID
       :return: Examination Object
    """
    return Examination.objects.get(exID=exID)


def update_examination(exID: AutoField, exDate: date, pat: Patient):
    """
          Update Examination

          :param exID: id of examination
          :param exDate: date of examination
          :return: Examination Object
       """
    examination = Examination.objects.get(exID=exID)
    examination.date = exDate
    examination.pat = pat
    examination.save()
    return examination


def delete_examination(exID: AutoField):
    """
          Delete Examination

          :param exID: id of examination
       """
    examination = Examination.objects.get(exID=exID)
    examination.delete()


def get_all_examinations():
    """
        get all Examinations
    """
    return Examination.objects.all()
