from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from myapi.cruds.crud_point import create_point, get_point_by_id, delete_point, update_point


class TestPointMethods(TestCase):

    def test_create_point_valid(self):
        p = create_point(2, 4, 1)
        self.assertEqual(p.x, 2)
        self.assertEqual(p.y, 4)
        self.assertEqual(p.quadrant, 1)

    def test_create_point_invalid_quadrant(self):
        with self.assertRaises(ValueError):
            create_point(2, 4, 6)

    def test_get_point_valid_id(self):
        p1 = create_point(2, 4, 1)
        p2 = get_point_by_id(p1.pID)
        self.assertEqual(p1, p2)

    def test_get_point_invalid_id(self):
        with self.assertRaises(ObjectDoesNotExist):
            get_point_by_id(-1)

    def test_update_point_valid(self):
        pOld = create_point(1, 3, 1)
        pNew = update_point(pOld.pID, 2, 4, 1)
        pCorr = create_point(2, 4, 1)
        self.assertEqual(pNew.x, pCorr.x)
        self.assertEqual(pNew.y, pCorr.y)
        self.assertEqual(pNew.quadrant, pCorr.quadrant)

    def test_update_point_invalid_quadrant(self):
        with self.assertRaises(ValueError):
            pOld = create_point(1, 3, 1)
            pNew = update_point(pOld.pID, 2, 4, 6)
            pCorr = None
            self.assertEqual(pNew, pCorr)

    def test_delete_point_valid(self):
        p = create_point(2, 3, 1)
        pID = p.pID
        get_point_by_id(pID)
        delete_point(p.pID)
        with self.assertRaises(ObjectDoesNotExist):
            get_point_by_id(pID)

    def test_delete_point_invalid(self):
        with self.assertRaises(ObjectDoesNotExist):
            create_point(2, 3, 1)
            pID = -1
            delete_point(pID)


