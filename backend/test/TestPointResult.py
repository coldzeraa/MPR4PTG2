import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from myapi.cruds.crud_point_result import (create_point_result,
                                           get_point_result_by_id,
                                           update_point_result,
                                           delete_point_result)
from myapi.cruds.crud_point import create_point
from myapi.cruds.crud_examination import create_examination
from myapi.cruds.crud_patient import create_patient


class TestPointResultMethods(TestCase):

    def test_create_point_result_valid(self):
        p = create_point(2, 4, 1)
        pat = create_patient()
        ex = create_examination(datetime.date.today(), pat)
        pr = create_point_result(True, p, ex)
        self.assertEqual(pr.seen, True)
        self.assertEqual(pr.p, p)
        self.assertEqual(pr.ex, ex)

    def test_get_point_result_valid_id(self):
        p = create_point(2, 4, 1)
        pat = create_patient()
        ex = create_examination(datetime.date.today(), pat)
        pr1 = create_point_result(True, p, ex)
        pr2 = get_point_result_by_id(pr1.resID)
        self.assertEqual(pr1, pr2)


    def test_get_point_result_invalid_id(self):
        with self.assertRaises(ObjectDoesNotExist):
            get_point_result_by_id(-1)

    def test_update_point_result_valid(self):
        p = create_point(2, 4, 1)
        pat = create_patient()
        ex = create_examination(datetime.date.today(), pat)
        prOld = create_point_result(True, p, ex)
        prNew = update_point_result(prOld.resID, False, p, ex)
        prCorr = create_point_result(False, p, ex)
        self.assertEqual(prNew.seen, prCorr.seen)
        self.assertEqual(prNew.ex, prCorr.ex)
        self.assertEqual(prNew.p, prCorr.p)

    def test_delete_point_result_valid(self):
        p = create_point(2, 4, 1)
        pat = create_patient()
        ex = create_examination(datetime.date.today(), pat)
        pr = create_point_result(True, p, ex)
        delete_point_result(pr.resID)
        with self.assertRaises(ObjectDoesNotExist):
            get_point_result_by_id(pr.resID)

    def test_delete_point_result_invalid(self):
        with self.assertRaises(ObjectDoesNotExist):
            delete_point_result(-1)



