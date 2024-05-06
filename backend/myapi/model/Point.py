class Point:

    def __init__(self, x, y, quadrant):
        self._x = x
        self._y = y
        self._quadrant = quadrant

    # Getter method for x
    def get_x(self):
        return self._x

    # Setter method for x
    def set_x(self, x):
        self._x = x

    # Getter method for y
    def get_y(self):
        return self._y

    # Setter method for y
    def set_y(self, y):
        self._y = y

    # Getter method for quadrant
    def get_quadrant(self):
        return self._quadrant

    # Setter method for quadrant
    def set_quadrant(self, quadrant):
        self._quadrant = quadrant

    def __str__(self):
        return f"({self._x}|{self._y})"
