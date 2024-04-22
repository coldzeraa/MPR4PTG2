from myapi.models import Patient


def create_patient(lastName: str, firstName: str, email: str):
    """
        Create a new Patient object

        :param id: id of patient
        :param lastName: last name of patient
        :param firstName: first name of patient
        :param email: email of patient
        :return: new patient
    """
    return Patient.objects.create(lastName=lastName, firstName=firstName, email=email)


def get_patient_by_id(id: int):
    """
       Get Patient by given id

       :param id: id of patient
       :return: Patient Object
    """
    return Patient.objects.get(id=id)


def update_patient(id: int, firstName: str, lastName: str, email: str):
    """
          Update Patient

          :param id: id of patient
          :param firstName: first name of patient
          :param lastName: last name of patient
          :param email: email of patient
          :return: Patient Object
       """
    patient = Patient.objects.get(id)
    patient.lastName = lastName
    patient.firstName = firstName
    patient.email = email
    patient.save()
    return patient


def delete_patient(id: int):
    """
          Delete Patient

          :param id: id of patient
       """
    patient = Patient.objects.get(id=id)
    patient.delete()

