from django.db.models import AutoField
from typing import Dict, List

from myapi.models import Patient


def create_patient(firstName: str, lastName: str, email: str, password: str):
    """
        Create a new Patient object

        :param lastName: last name of patient
        :param firstName: first name of patient
        :param email: email of the patient
        :param password: password of patient
        :return: new patient
    """
    
    return Patient.objects.create(firstName=firstName, lastName=lastName, email=email, password=password)
    

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
    # TODO maybe add email
    """
        Update Patient

        :param patID: id of patient
        :param firstName: first name of patient
        :param lastName: last name of patient
        :param password: password of patient
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

def filter_patients(filter_criteria: Dict[str, any]) -> List[Patient]:
    """
    Filter patients based on specified criteria.

    :param filter_criteria: Dictionary of field names and values to filter by
    :return: QuerySet of Patient objects matching the criteria
    """
    return Patient.objects.filter(**filter_criteria)


def get_patient_by_email(email: str):
    return Patient.objects.get(email = email)