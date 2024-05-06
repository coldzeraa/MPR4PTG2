class Examination:
    def __init__(self, exID, date, patient):
        self.exID = exID
        self.date = date
        self.patient = patient

    # Getter method for exID
    def get_exID(self):
        return self.exID

    # Setter method for exID
    def set_exID(self, exID):
        self.exID = exID

    # Getter method for date
    def get_date(self):
        return self.date

    # Setter method for date
    def set_date(self, date):
        self.date = date

    # Getter method for patient
    def get_patient(self):
        return self.patient

    # Setter method for patient
    def set_patient(self, patient):
        self.patient = patient

    def __str__(self):
        return f"Examination ID: {self.exID}, Date: {self.date}, Patient: {self.patient}"
