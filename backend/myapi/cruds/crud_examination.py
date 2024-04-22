from datetime import date

from backend.myapi.models import Examination


def create_examination(examinationID: int, exDate: date, pID: int):
    """
        Create a new Examination object

        :param examinationID: examination ID
        :param exDate: date of examination
        :param pID: patient ID
        :return: new examination
       """
    return Examination.objects.create(exID=examinationID, date=exDate, pID=pID)


def get_examination_by_id(exID: int):
    """
       Get Examination by given ID

       :param exID: examination ID
       :return: Examination Object
    """
    return Examination.objects.get(exID=exID)


def update_examination(exID: int, exDate: date):
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


def delete_examination(exID: int):
    """
          Delete Examination

          :param exID: id of examination
       """
    examination = Examination.objects.get(exID=exID)
    examination.delete()
