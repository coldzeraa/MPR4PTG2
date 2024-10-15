class Point:

    def __init__(self, x, y, quadrant):
        """
        Initializes a Point object with the given x and y coordinates, and the quadrant.

        :param x: The x coordinate of the point
        :param y: The y coordinate of the point
        :param quadrant: The quadrant where the point is located
        """
        self._x = x
        self._y = y
        self._quadrant = quadrant

    # Getter method for x
    def get_x(self):
        """
        Returns the x coordinate of the point.

        :return: The x coordinate
        """
        return self._x

    # Setter method for x
    def set_x(self, x):
        """
        Sets the x coordinate of the point.

        :param x: The new x coordinate
        :return: None
        """
        self._x = x

    # Getter method for y
    def get_y(self):
        """
        Returns the y coordinate of the point.

        :return: The y coordinate
        """
        return self._y

    # Setter method for y
    def set_y(self, y):
        """
        Sets the y coordinate of the point.

        :param y: The new y coordinate
        :return: None
        """
        self._y = y

    # Getter method for quadrant
    def get_quadrant(self):
        """
        Returns the quadrant where the point is located.

        :return: The quadrant
        """
        return self._quadrant

    # Setter method for quadrant
    def set_quadrant(self, quadrant):
        """
        Sets the quadrant where the point is located.

        :param quadrant: The new quadrant
        :return: None
        """
        self._quadrant = quadrant

    def __str__(self):
        """
        Returns a string representation of the Point object in the format '(x|y)'.

        :return: A string with the x and y coordinates of the point
        """
        return f"({self._x}|{self._y})"
