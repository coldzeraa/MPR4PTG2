class PointResult:
    def __init__(self, resID, seen, point, examination):
        """
        Initializes a PointResult object with the given result ID, seen status, point, and examination.

        :param resID: The ID of the point result
        :param seen: A boolean indicating whether the point has been seen
        :param point: The point associated with the result
        :param examination: The examination associated with the result
        """
        self.resID = resID
        self.seen = seen
        self.point = point
        self.examination = examination

    # Getter method for resID
    def get_resID(self):
        """
        Returns the result ID.

        :return: The ID of the point result
        """
        return self.resID

    # Setter method for resID
    def set_resID(self, resID):
        """
        Sets the result ID.

        :param resID: The new ID of the point result
        :return: None
        """
        self.resID = resID

    # Getter method for seen
    def get_seen(self):
        """
        Returns the seen status of the point result.

        :return: A boolean indicating whether the point has been seen
        """
        return self.seen

    # Setter method for seen
    def set_seen(self, seen):
        """
        Sets the seen status of the point result.

        :param seen: A boolean indicating whether the point has been seen
        :return: None
        """
        self.seen = seen

    # Getter method for point
    def get_point(self):
        """
        Returns the point associated with the result.

        :return: The point object
        """
        return self.point

    # Setter method for point
    def set_point(self, point):
        """
        Sets the point associated with the result.

        :param point: The new point object
        :return: None
        """
        self.point = point

    # Getter method for examination
    def get_examination(self):
        """
        Returns the examination associated with the point result.

        :return: The examination object
        """
        return self.examination

    # Setter method for examination
    def set_examination(self, examination):
        """
        Sets the examination associated with the point result.

        :param examination: The new examination object
        :return: None
        """
        self.examination = examination

    def __str__(self):
        """
        Returns a string representation of the PointResult object.

        :return: A string with the result ID, seen status, point, and examination details
        """
        return f"Result ID: {self.resID}, Seen: {self.seen}, Point: {self.point}, Examination: {self.examination}"
