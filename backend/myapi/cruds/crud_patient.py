from django.db.models import AutoField

from myapi.models import Patient

DEFAULT_FIRSTNAME = "John"
DEFAULT_LASTNAME = "Doe"
DEFAULT_EMAIL = "unknown"

def create_patient(firstName: str = "", lastName: str = "", email: str = ""):
    """
        Create a new Patient object

        :param lastName: last name of patient
        :param firstName: first name of patient
        :param email: email of the patient
        :return: new patient
    """
    if firstName == "" or lastName == "":
        firstName = DEFAULT_FIRSTNAME
        lastName = DEFAULT_LASTNAME
    if email == "":
        email = DEFAULT_EMAIL
    return Patient.objects.create(firstName=firstName, lastName=lastName, email=email)


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

