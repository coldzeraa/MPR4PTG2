class Patient:
    def __init__(self, patID, lastName, firstName, password, email=None):
        """
        Initializes a Patient object with the given patient ID, last name, first name, and optional email address.

        :param patID: The ID of the patient
        :param lastName: The last name of the patient
        :param firstName: The first name of the patient
        :param password: Hashed password of the patient
        :param email: (Optional) The email address of the patient
        """
        self.patID = patID
        self.lastName = lastName
        self.firstName = firstName
        self.password = password
        self.email = email

    # Getter method for patID
    def get_patID(self):
        """
        Returns the patient ID.

        :return: The ID of the patient
        """
        return self.patID

    # Setter method for patID
    def set_patID(self, patID):
        """
        Sets the patient ID.

        :param patID: The new ID of the patient
        :return: None
        """
        self.patID = patID

    # Getter method for lastName
    def get_lastName(self):
        """
        Returns the last name of the patient.

        :return: The last name of the patient
        """
        return self.lastName

    # Setter method for lastName
    def set_lastName(self, lastName):
        """
        Sets the last name of the patient.

        :param lastName: The new last name of the patient
        :return: None
        """
        self.lastName = lastName

    # Getter method for firstName
    def get_firstName(self):
        """
        Returns the first name of the patient.

        :return: The first name of the patient
        """
        return self.firstName

    # Setter method for firstName
    def set_firstName(self, firstName):
        """
        Sets the first name of the patient.

        :param firstName: The new first name of the patient
        :return: None
        """
        self.firstName = firstName

    # Getter method for password
    def get_password(self):
        """
        Returns the hashed password of the patient.

        :return: The hashed password of the patient
        """
        return self.password

    # Setter method for password
    def set_password(self, password):
        """
        Sets the hasehed password of the patient.

        :param password: The new password of the patient
        :return: None
        """
        self.password = password

    # Getter method for email
    def get_email(self):
        """
        Returns the email address of the patient.

        :return: The email address of the patient
        """
        return self.email

    # Setter method for email
    def set_email(self, email):
        """
        Sets the email address of the patient.

        :param email: The new email address of the patient
        :return: None
        """
        self.email = email

    def __str__(self):
        """
        Returns a string representation of the Patient object in the format 'lastName firstName (email)'.

        :return: A string with the patient's last name, first name, and email address (if available)
        """
        return f"{self.lastName} {self.firstName} ({self.email})"
