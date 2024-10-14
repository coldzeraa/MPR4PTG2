class Examination:
    def __init__(self, exID, date, patient):
        """
        Initializes an Examination object with the given examination ID, date, and patient information.

        :param exID: The ID of the examination
        :param date: The date of the examination
        :param patient: The patient associated with the examination
        """
        self.exID = exID
        self.date = date
        self.patient = patient

    # Getter method for exID
    def get_exID(self):
        """
        Returns the examination ID.

        :return: The ID of the examination
        """
        return self.exID

    # Setter method for exID
    def set_exID(self, exID):
        """
        Sets the examination ID.

        :param exID: The new ID of the examination
        :return: None
        """
        self.exID = exID

    # Getter method for date
    def get_date(self):
        """
        Returns the date of the examination.

        :return: The date of the examination
        """
        return self.date

    # Setter method for date
    def set_date(self, date):
        """
        Sets the date of the examination.

        :param date: The new date of the examination
        :return: None
        """
        self.date = date

    # Getter method for patient
    def get_patient(self):
        """
        Returns the patient associated with the examination.

        :return: The patient object
        """
        return self.patient

    # Setter method for patient
    def set_patient(self, patient):
        """
        Sets the patient associated with the examination.

        :param patient: The new patient object
        :return: None
        """
        self.patient = patient

    def __str__(self):
        """
        Returns a string representation of the Examination object.

        :return: A string with the examination ID, date, and patient information
        """
        return f"Examination ID: {self.exID}, Date: {self.date}, Patient: {self.patient}"
