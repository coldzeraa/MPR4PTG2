from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

import myapi.db.PointService as PS


class TestPointServiceMethods(TestCase):

    def test_store_point_valid(self):
        p = PS.PointService.store(2, 4, 1)
        self.assertEqual(p.x, 2)
        self.assertEqual(p.y, 4)
        self.assertEqual(p.quadrant, 1)

    def test_store_point_invalid_quadrant(self):
        with self.assertRaises(ValueError):
            PS.PointService.store(2, 4, 6)

    def test_get_point_valid_id(self):
        p1 = PS.PointService.store(2, 4, 1)
        p2 = PS.PointService.get(p1.pID)
        self.assertEqual(p1, p2)

    def test_get_point_invalid_id(self):
        with self.assertRaises(ObjectDoesNotExist):
            PS.PointService.get(-1)

    def test_update_point_valid(self):
        pOld = PS.PointService.store(1, 3, 1)
        pNew = PS.PointService.update(pOld.pID, 2, 4, 1)
        pCorr = PS.PointService.store(2, 4, 1)
        self.assertEqual(pNew.x, pCorr.x)
        self.assertEqual(pNew.y, pCorr.y)
        self.assertEqual(pNew.quadrant, pCorr.quadrant)

    def test_update_point_invalid_quadrant(self):
        with self.assertRaises(ValueError):
            pOld = PS.PointService.store(1, 3, 1)
            pNew = PS.PointService.update(pOld.pID, 2, 4, 6)
            pCorr = None
            self.assertEqual(pNew, pCorr)

    def test_delete_point_valid(self):
        p = PS.PointService.store(2, 3, 1)
        pID = p.pID
        PS.PointService.delete(p.pID)
        with self.assertRaises(ObjectDoesNotExist):
            PS.PointService.get(pID)

    def test_delete_point_invalid(self):
        with self.assertRaises(ObjectDoesNotExist):
            PS.PointService.delete(-1)
