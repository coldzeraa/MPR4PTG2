import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

import myapi.db.PointResultService as PRS

from myapi.cruds.crud_point import create_point
from myapi.cruds.crud_examination import create_examination
from myapi.cruds.crud_patient import create_patient

class TestPointResultServiceMethods(TestCase):

    def test_store_point_result_valid(self):
        p = create_point(2, 4, 1)
        pat = create_patient()
        ex = create_examination(datetime.date.today(), pat)
        pr = PRS.PointResultService.store(True, p, ex)
        self.assertEqual(pr.seen, True)
        self.assertEqual(pr.p, p)
        self.assertEqual(pr.ex, ex)

    def test_get_point_result_valid_id(self):
        p = create_point(2, 4, 1)
        pat = create_patient()
        ex = create_examination(datetime.date.today(), pat)
        pr1 = PRS.PointResultService.store(True, p, ex)
        pr2 = PRS.PointResultService.get(pr1.resID)
        self.assertEqual(pr1, pr2)

    def test_get_point_result_invalid_id(self):
        with self.assertRaises(ObjectDoesNotExist):
            PRS.PointResultService.get(-1)

    def test_update_point_result_valid(self):
        p = create_point(2, 4, 1)
        pat = create_patient()
        ex = create_examination(datetime.date.today(), pat)
        prOld = PRS.PointResultService.store(True, p, ex)
        prNew = PRS.PointResultService.update(prOld.resID, False, p, ex)
        prCorr = PRS.PointResultService.store(False, p, ex)
        self.assertEqual(prNew.seen, prCorr.seen)
        self.assertEqual(prNew.ex, prCorr.ex)
        self.assertEqual(prNew.p, prCorr.p)

    def test_delete_point_result_valid(self):
        p = create_point(2, 4, 1)
        pat = create_patient()
        ex = create_examination(datetime.date.today(), pat)
        pr = PRS.PointResultService.store(True, p, ex)
        PRS.PointResultService.delete(pr.resID)
        with self.assertRaises(ObjectDoesNotExist):
            PRS.PointResultService.get(pr.resID)

    def test_delete_point_result_invalid(self):
        with self.assertRaises(ObjectDoesNotExist):
            PRS.PointResultService.delete(-1)



