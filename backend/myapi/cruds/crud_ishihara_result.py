from django.db.models import AutoField

from myapi.models import ResultIshihara
from myapi.model.Examination import Examination

 
def create_ishihara_result(filename: str, recognized: bool, ex: Examination):
    """
        Create a new IshiharaResult Object

        :param filename: name of affected file
        :param recognized: specifies if image was recognized 
        :param ex: examination
        :return: new PointResult
       """
       
    return ResultIshihara.objects.create(filename=filename, recognized=recognized, ex=ex)


def get_all_ishihara_results():
    """
       Get all IshiharaResult
    """
    return ResultIshihara.objects.all()


def get_ishihara_result_by_id(resID: AutoField):
    """
       Get IshiharaResult by given ID

       :param resID: IshiharaResult ID
       :return: IshiharaResult Object
    """
    return ResultIshihara.objects.get(resID=resID)


def update_ishihara_result(resID: AutoField, filename: str, recognized: bool,  exID: AutoField):
    """
          Update IshiharaResult

          :param resID: id of IshiharaResult
          :param filename: name of affected file
          :param recognized: specifies if image was recognized 
          :return: PatientResult Object
       """
    ishihara_result = ResultIshihara.objects.get(resID=resID)
    ishihara_result.filename = filename
    ishihara_result.recognized = recognized
    ishihara_result.ex = exID
    ishihara_result.save()
    return ishihara_result


def delete_ishihara_result(resID: AutoField):
    """
          Delete IshiharaResult

          :param resID: id of IshiharaResult
       """
    point_result = ResultIshihara.objects.get(resID=resID)
    point_result.delete()
    
    
def get_ishihara_result_by_exID(exID: AutoField):
    """
        Returns IshiharaResult of given exID

        :param exID: id of examination
    """
    
    return ResultIshihara.objects.filter(ex = exID)
    
    
    
