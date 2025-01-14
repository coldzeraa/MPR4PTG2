class IshiharaResult:
    def __init__(self, resID, recognized, filename, examination):
        """
        Initializes a object with the given result ID, recognizing status, filename, and examination.

        :param resID: The ID of the point result
        :param recognized: A boolean indicating whether the number was identified correctly
        :param filename: The name of the file
        :param examination: The examination associated with the result
        """
        self.resID = resID
        self.recognized = recognized
        self.filename = filename
        self.examination = examination

    def get_resID(self):
        """
        Returns the result ID.

        :return: The ID of the IshiharaResult
        """
        return self.resID

    def set_resID(self, resID):
        """
        Sets the result ID.

        :param resID: The new ID of the IshiharaResult
        :return: None
        """
        self.resID = resID

    def set_recognized(self, recognized):
        """
        Sets the result ID.

        :param resID: The new ID of the IshiharaResult
        :return: None
        """
        self.recognized = recognized

    def get_recognized(self):
        """
        Returns the seen status of the IshiharaResult.

        :return: A boolean indicating whether the number was recognized
        """
        return self.recognized

    def set_filename(self, filename):
        """
        Sets the filename of the result.

        :param seen: The filename
        :return: None
        """
        self.filename = filename

    def get_examination(self):
        """
        Returns the examination associated with the point result.

        :return: The examination object
        """
        return self.examination

    def set_examination(self, examination):
        """
        Sets the examination associated with the point result.

        :param examination: The new examination object
        :return: None
        """
        self.examination = examination