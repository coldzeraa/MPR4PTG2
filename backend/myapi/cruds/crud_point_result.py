from django.db.models import AutoField

from myapi.models import PointResult


def create_point_result(seen: bool, pID: int, exID: int):
    """
        Create a new PointResult Object

        :param seen: specifies if Point was recognized
        :param pID: patient ID
        :param exID: examination ID
        :return: new PointResult
       """
    return PointResult.objects.create(seen=seen, p=pID, ex=exID)


def get_all_point_results():
    """
       Get all PointResults
    """
    return PointResult.objects.all()


def get_point_result_by_id(resID: AutoField):
    """
       Get PointResult by given ID

       :param resID: point result ID
       :return: PointResult Object
    """
    return PointResult.objects.get(resID=resID)


def update_point_result(resID: AutoField, seen: bool, pID: AutoField,  exID: AutoField):
    """
          Update PointResult

          :param resID: id of point result
          :param seen: point seen by patient (true|false)
          :return: PatientResult Object
       """
    point_result = PointResult.objects.get(resID=resID)
    point_result.seen = seen
    point_result.ex = exID
    point_result.p = pID
    point_result.save()
    return point_result


def delete_point_result(resID: AutoField):
    """
          Delete PointResult

          :param resID: id of point result
       """
    point_result = PointResult.objects.get(resID=resID)
    point_result.delete()
