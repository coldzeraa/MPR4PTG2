from django.db.models import AutoField

from backend.myapi.models import Patient


def create_patient(lastName: str, firstName: str):
    """
        Create a new Patient object

        :param patID: id of patient
        :param lastName: last name of patient
        :param firstName: first name of patient
        :return: new patient
    """
    return Patient.objects.create(lastName=lastName, firstName=firstName)


def get_patient_by_id(patID: AutoField):
    """
       Get Patient by given id

       :param patID: id of patient
       :return: Patient Object
    """
    return Patient.objects.get(id=id)


def update_patient(patID: AutoField, firstName: str, lastName: str):
    """
          Update Patient

          :param patID: id of patient
          :param firstName: first name of patient
          :param lastName: last name of patient
          :return: Patient Object
       """
    patient = Patient.objects.get(id)
    patient.lastName = lastName
    patient.firstName = firstName
    patient.save()
    return patient


def delete_patient(patID: AutoField):
    """
          Delete Patient

          :param id: id of patient
       """
    patient = Patient.objects.get(id=id)
    patient.delete()

