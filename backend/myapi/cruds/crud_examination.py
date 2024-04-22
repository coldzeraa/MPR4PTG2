from datetime import date

from myapi.models import Examination, Patient
from django.db.models import AutoField


def create_examination(exDate: date, pID: AutoField):
    """
        Create a new Examination object

        :param exDate: date of examination
        :param pID: patient ID
        :return: new examination
       """
    patient = Patient.objects.get(patID=pID)
    return Examination.objects.create(date=exDate, patientID=patient)


def get_examination_by_id(exID: AutoField):
    """
       Get Examination by given ID

       :param exID: examination ID
       :return: Examination Object
    """
    return Examination.objects.get(exID=exID)


def update_examination(exID: AutoField, exDate: date):
    """
          Update Examination

          :param exID: id of examination
          :param exDate: date of examination
          :return: Examination Object
       """
    examination = Examination.objects.get(exID=exID)
    examination.date = exDate
    examination.save()
    return examination


def delete_examination(exID: AutoField):
    """
          Delete Examination

          :param exID: id of examination
       """
    examination = Examination.objects.get(exID=exID)
    examination.delete()
