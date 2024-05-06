class PointResult:
    def __init__(self, resID, seen, point, examination):
        self.resID = resID
        self.seen = seen
        self.point = point
        self.examination = examination

    # Getter method for resID
    def get_resID(self):
        return self.resID

    # Setter method for resID
    def set_resID(self, resID):
        self.resID = resID

    # Getter method for seen
    def get_seen(self):
        return self.seen

    # Setter method for seen
    def set_seen(self, seen):
        self.seen = seen

    # Getter method for point
    def get_point(self):
        return self.point

    # Setter method for point
    def set_point(self, point):
        self.point = point

    # Getter method for examination
    def get_examination(self):
        return self.examination

    # Setter method for examination
    def set_examination(self, examination):
        self.examination = examination

    def __str__(self):
        return f"Result ID: {self.resID}, Seen: {self.seen}, Point: {self.point}, Examination: {self.examination}"
