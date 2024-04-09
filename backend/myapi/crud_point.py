from models import Point


def create_point(x: int, y: int, q: int):
    """
        Create a new Point object

        :param x: x coordinate
        :param y: y coordinate
        :param q: quadrant
        :return: new point
    """
    if valid_quadrant(q):
        return Point.objects.create(x=x, y=y, quadrant=q)


def get_point_by_id(pID: int):
    """
       Get PointResult by given ID

       :param pID: point ID
       :return: PointResult Object
    """
    return Point.objects.get(pID=pID)


def update_point(pID: int, x: int, y: int, quadrant: int):
    """
       Update Point, set given parameters

       :param pID: point ID
       :param x: x coordinate
       :param y: y coordinate
       :param quadrant: quadrant of the point
       :return: Patient Object
    """
    point = Point.objects.get(pID=pID)
    point.x = x
    point.y = y
    point.quadrant = quadrant
    point.save()
    return point


def delete_point(pID: int):
    """
          Delete Examination

          :param pID: id of examination
       """
    point = Point.objects.get(pID=pID)
    point.delete()


def valid_quadrant(q: int):
    return 1 <= q <= 4
