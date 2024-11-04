from django.db.models import AutoField

from myapi.models import ResultPerimetry
from myapi.model.Point import Point
from myapi.model.Examination import Examination


def create_perimetry_result(seen: bool, p: Point, ex: Examination):
    """
        Create a new PointResult Object

        :param seen: specifies if Point was recognized
        :param p: patient 
        :param ex: examination 
        :return: new PointResult
       """
       
    return ResultPerimetry.objects.create(seen=seen, p=p, ex=ex)


def get_all_perimetry_results():
    """
       Get all PointResults
    """
    return ResultPerimetry.objects.all()


def get_perimetry_result_by_id(resID: AutoField):
    """
       Get PointResult by given ID

       :param resID: point result ID
       :return: PointResult Object
    """
    return ResultPerimetry.objects.get(resID=resID)


def update_perimetry_result(resID: AutoField, seen: bool, pID: AutoField,  exID: AutoField):
    """
          Update PointResult

          :param resID: id of point result
          :param seen: point seen by patient (true|false)
          :return: PatientResult Object
       """
    point_result = ResultPerimetry.objects.get(resID=resID)
    point_result.seen = seen
    point_result.ex = exID
    point_result.p = pID
    point_result.save()
    return point_result


def delete_perimetry_result(resID: AutoField):
    """
          Delete PointResult

          :param resID: id of point result
       """
    point_result = ResultPerimetry.objects.get(resID=resID)
    point_result.delete()
    
    
def get_perimetry_result_by_exID(exID: AutoField):
    """
        Returns PointResults of given exID

        :param exID: id of examination
    """
    
    return ResultPerimetry.objects.filter(ex = exID)
    
    
    
