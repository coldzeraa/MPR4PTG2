from django.core.exceptions import ObjectDoesNotExist
from django.db.models import AutoField

from myapi.models import Point


def create_point(x: int, y: int, q: int):
    """
        Create a new Point object

        :param x: x coordinate
        :param y: y coordinate
        :param q: quadrant
        :return: new point
    """
    if not valid_quadrant(q):
        raise ValueError("Invalid quadrant value")
    
    # Hash primary key
    id = x * 100 + y

    return Point.objects.create(pID=id, x=x, y=y, quadrant=q)


def get_all_points():
    """
       Get all Points
    """
    return Point.objects.all()



def get_points_by_quadrant(quadrant: int):
    """
       Get all Points from a specific quadrant
    """
    if valid_quadrant(quadrant):
        return Point.objects.filter(quadrant=quadrant)

    else:
        raise RuntimeError


def get_point_by_id(pID: int):
    """
       Get Point by given ID

       :param pID: point ID
       :return: Point Object
    """
    print(pID)
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
    if not valid_quadrant(quadrant):
        raise ValueError("Invalid quadrant value")

    point = Point.objects.get(pID=pID)
    point.x = x
    point.y = y
    point.quadrant = quadrant
    point.save()
    return point


def delete_point(pID: int):
    """
    Delete Point

    :param pID: id of point
    """
    (Point.objects.get(pID=pID)).delete()
    

def get_point_by_x_and_y(x: int, y: int):
    return Point.objects.get(x=x, y=y)


def valid_quadrant(q: int):
    return 1 <= q <= 4