from datetime import datetime, timezone

from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from myapi.cruds.crud_ishihara_result import (create_ishihara_result,
                                           get_ishihara_result_by_id,
                                           update_ishihara_result,
                                           delete_ishihara_result)
from myapi.cruds.crud_examination import create_examination
from myapi.cruds.crud_patient import create_patient


class TestPointResultMethods(TestCase):

    def test_create_ishihara_result_valid(self):
        fileName = "some_filename"
        pat = create_patient("Max", "Mustermann", "max.mustermann@gmail.com", "SOME_PASSWORD")
        ex = create_examination(datetime.now(timezone.utc), pat, "I")
        ir = create_ishihara_result(fileName, True, ex)
        self.assertEqual(ir.recognized, True)
        self.assertEqual(ir.filename, fileName)
        self.assertEqual(ir.ex, ex)

    def test_get_ishihara_result_valid_id(self):
        fileName = "some_filename"
        pat = create_patient("Max", "Mustermann", "max.mustermann@gmail.com", "SOME_PASSWORD")
        ex = create_examination(datetime.now(timezone.utc), pat, "P")
        ir1 = create_ishihara_result(fileName, False, ex)
        ir2 = get_ishihara_result_by_id(ir1.resID)
        self.assertEqual(ir1, ir2)


    def test_get_ishihara_result_invalid_id(self):
        with self.assertRaises(ObjectDoesNotExist):
            get_ishihara_result_by_id(-1)

    def test_update_ishihara_result_valid(self):
        fileName = "some_filename"
        pat = create_patient("Max", "Mustermann", "max.mustermann@gmail.com", "SOME_PASSWORD")
        ex = create_examination(datetime.now(timezone.utc), pat, "P")
        irOld = create_ishihara_result(fileName, True, ex)
        irNew = update_ishihara_result(irOld.resID, fileName, False, ex)
        irCorr = create_ishihara_result(fileName, False, ex)
        self.assertEqual(irNew.recognized, irCorr.recognized)
        self.assertEqual(irNew.ex, irCorr.ex)
        self.assertEqual(irNew.filename, irCorr.filename)

    def test_delete_ishihara_result_valid(self):
        fileName = "some_filename"
        pat = create_patient("Max", "Mustermann", "max.mustermann@gmail.com", "SOME_PASSWORD")
        ex = create_examination(datetime.now(timezone.utc), pat, "P")
        ir = create_ishihara_result(fileName, True, ex)
        delete_ishihara_result(ir.resID)
        with self.assertRaises(ObjectDoesNotExist):
            get_ishihara_result_by_id(ir.resID)

    def test_delete_ishihara_result_invalid(self):
        with self.assertRaises(ObjectDoesNotExist):
            delete_ishihara_result(-1)



