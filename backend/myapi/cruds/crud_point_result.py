from backend.myapi.models import PointResult


def create_point_result(resultID: int, seen: bool, pID: int, exID: int):
    """
        Create a new PointResult Object

        :param resultID: result ID
        :param seen: specifies if Point was recognized
        :param pID: patient ID
        :param exID: examination ID
        :return: new PointResult
       """
    return PointResult.objects.create(resID=resultID, seen=seen, point=pID, examination=exID)


def get_point_result_by_id(resID: int):
    """
       Get PointResult by given ID

       :param resID: point result ID
       :return: PointResult Object
    """
    return PointResult.objects.get(resID=resID)


def update_point_result(resID: int, seen: bool):
    """
          Update PointResult

          :param resID: id of point result
          :param seen: point seen by patient (true|false)
          :return: PatientResult Object
       """
    point_result = PointResult.objects.get(resID=resID)
    point_result.seen = seen
    point_result.save()
    return point_result


def delete_point_result(resID: int):
    """
          Delete PointResult

          :param resID: id of point result
       """
    point_result = PointResult.objects.get(resID=resID)
    point_result.delete()
