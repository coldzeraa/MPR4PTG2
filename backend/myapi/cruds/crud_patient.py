from django.db.models import AutoField

from backend.myapi.models import Patient


def create_patient(pID: AutoField, lastName: str, firstName: str):
    """
        Create a new Patient object

        :param id: id of patient
        :param lastName: last name of patient
        :param firstName: first name of patient
        :return: new patient
    """
    return Patient.objects.create(id=id, lastName=lastName, firstName=firstName)


def get_patient_by_id(pID: AutoField):
    """
       Get Patient by given id

       :param id: id of patient
       :return: Patient Object
    """
    return Patient.objects.get(id=id)


def update_patient(pID: AutoField, firstName: str, lastName: str):
    """
          Update Patient

          :param id: id of patient
          :param firstName: first name of patient
          :param lastName: last name of patient
          :return: Patient Object
       """
    patient = Patient.objects.get(id)
    patient.lastName = lastName
    patient.firstName = firstName
    patient.save()
    return patient


def delete_patient(pID: AutoField):
    """
          Delete Patient

          :param id: id of patient
       """
    patient = Patient.objects.get(id=id)
    patient.delete()

