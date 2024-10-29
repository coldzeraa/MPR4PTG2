from django.db.models import AutoField

from myapi.models import Patient

DEFAULT_FIRSTNAME = None
DEFAULT_LASTNAME = None
DEFAULT_EMAIL = None
DEFAULT_PASSWORD = None

def create_patient(firstName: str = "", lastName: str = "", password: str= "", email: str = ""):
    """
        Create a new Patient object

        :param lastName: last name of patient
        :param firstName: first name of patient
        :param passord: hashed password of patient
        :param email: email of the patient
        :return: new patient
    """
    if firstName == "" or lastName == "":
        firstName = DEFAULT_FIRSTNAME
        lastName = DEFAULT_LASTNAME
    if email == "":
        email = DEFAULT_EMAIL
    if password == "":
        password = DEFAULT_PASSWORD
    return Patient.objects.create(firstName=firstName, lastName=lastName, password=password, email=email)


def get_all_patients():
    """
       Get all Patients
    """
    return Patient.objects.all()


def get_patient_by_id(patID: AutoField):
    """
       Get Patient by given id

       :param patID: id of patient
       :return: Patient Object
    """
    return Patient.objects.get(patID=patID)


def update_patient(patID: AutoField, firstName: str, lastName: str, password: str):
    """
        Update Patient

        :param patID: id of patient
        :param firstName: first name of patient
        :param lastName: last name of patient
        :param password: hashed password of the patient
        :return: Patient Object
    """
    patient = Patient.objects.get(patID=patID)  # Corrected from Patient.objects.get(patID)
    patient.lastName = lastName
    patient.firstName = firstName
    patient.password = password
    patient.save()
    return patient


def delete_patient(patID: AutoField):
    """
        Delete Patient

        :param patID: id of patient
    """
    patient = Patient.objects.get(patID=patID)  # Corrected from Patient.objects.get(patID=patID)
    patient.delete()


