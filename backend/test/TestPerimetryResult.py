from datetime import datetime, timezone

from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from myapi.cruds.crud_perimetry_result import (create_perimetry_result,
                                           get_perimetry_result_by_id,
                                           update_perimetry_result,
                                           delete_perimetry_result)
from myapi.cruds.crud_point import create_point
from myapi.cruds.crud_examination import create_examination
from myapi.cruds.crud_patient import create_patient


class TestPointResultMethods(TestCase):

    def test_create_perimetry_result_valid(self):
        p = create_point(2, 4, 1)
        pat = create_patient("Max", "Mustermann", "max.mustermann@gmail.com", "SOME_PASSWORD")
        ex = create_examination(datetime.now(timezone.utc), pat, "P")
        pr = create_perimetry_result(True, p, ex)
        self.assertEqual(pr.seen, True)
        self.assertEqual(pr.p, p)
        self.assertEqual(pr.ex, ex)

    def test_get_perimetry_result_valid_id(self):
        p = create_point(2, 4, 1)
        pat = create_patient("Max", "Mustermann", "max.mustermann@gmail.com", "SOME_PASSWORD")
        ex = create_examination(datetime.now(timezone.utc), pat, "P")
        pr1 = create_perimetry_result(True, p, ex)
        pr2 = get_perimetry_result_by_id(pr1.resID)
        self.assertEqual(pr1, pr2)


    def test_get_perimetry_result_invalid_id(self):
        with self.assertRaises(ObjectDoesNotExist):
            get_perimetry_result_by_id(-1)

    def test_update_perimetry_result_valid(self):
        p = create_point(2, 4, 1)
        pat = create_patient("Max", "Mustermann", "max.mustermann@gmail.com", "SOME_PASSWORD")
        ex = create_examination(datetime.now(timezone.utc), pat, "P")
        prOld = create_perimetry_result(True, p, ex)
        prNew = update_perimetry_result(prOld.resID, False, p, ex)
        prCorr = create_perimetry_result(False, p, ex)
        self.assertEqual(prNew.seen, prCorr.seen)
        self.assertEqual(prNew.ex, prCorr.ex)
        self.assertEqual(prNew.p, prCorr.p)

    def test_delete_perimetry_result_valid(self):
        p = create_point(2, 4, 1)
        pat = create_patient("Max", "Mustermann", "max.mustermann@gmail.com", "SOME_PASSWORD")
        ex = create_examination(datetime.now(timezone.utc), pat, "P")
        pr = create_perimetry_result(True, p, ex)
        delete_perimetry_result(pr.resID)
        with self.assertRaises(ObjectDoesNotExist):
            get_perimetry_result_by_id(pr.resID)

    def test_delete_perimetry_result_invalid(self):
        with self.assertRaises(ObjectDoesNotExist):
            delete_perimetry_result(-1)



