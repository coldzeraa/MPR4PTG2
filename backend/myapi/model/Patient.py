class Patient:
    def __init__(self, patID, lastName, firstName, email=None):
        self.patID = patID
        self.lastName = lastName
        self.firstName = firstName
        self.email = email

    # Getter method for patID
    def get_patID(self):
        return self.patID

    # Setter method for patID
    def set_patID(self, patID):
        self.patID = patID

    # Getter method for lastName
    def get_lastName(self):
        return self.lastName

    # Setter method for lastName
    def set_lastName(self, lastName):
        self.lastName = lastName

    # Getter method for firstName
    def get_firstName(self):
        return self.firstName

    # Setter method for firstName
    def set_firstName(self, firstName):
        self.firstName = firstName

    # Getter method for email
    def get_email(self):
        return self.email

    # Setter method for email
    def set_email(self, email):
        self.email = email

    def __str__(self):
        return f"{self.lastName} {self.firstName} ({self.email})"  # string representation as lastname firstname (email)
