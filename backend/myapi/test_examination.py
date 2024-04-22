import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from myapi.cruds.crud_examination import create_examination, get_examination_by_id, update_examination
from myapi.cruds.crud_patient import create_patient, delete_patient


class TestPointMethods(TestCase):
    def test_create_examination_valid(self):
        pat = create_patient("Martina", "Pletz")
        date = datetime.date.today()
        ex = create_examination(date, pat.patID)
        self.assertEqual(ex.pat, pat)
        self.assertEqual(ex.date, date)

    def test_get_examination_valid_id(self):
        pat1 = create_patient("David", "Derntl")
        date = datetime.date.today()
        ex1 = create_examination(date, pat1.patID)
        ex2 = get_examination_by_id(ex1.exID)
        self.assertEqual(ex1.date, ex2.date)
        self.assertEqual(ex1.pat, ex2.pat)

    def test_update_examination_valid(self):
        patOld = create_patient("Nico", "Pointner")
        patNew = create_patient("Eva", "Schoissengeier")
        date = datetime.date.today()
        exOld = create_examination(date, patOld.patID)
        exNew = update_examination(exOld.exID, date, patNew)
        self.assertEqual(exNew.pat, patNew)

    def test_delete_patient_valid(self):
        pat = create_patient("Elisabeth", "Mayrhuber")
        date = datetime.date.today()
        ex = create_examination(date, pat.patID)
        delete_patient(ex.exID)
        with self.assertRaises(ObjectDoesNotExist):
            get_examination_by_id(ex.exID)

    def test_delete_point_invalid(self):
        with self.assertRaises(ObjectDoesNotExist):
            delete_patient(-1)





