from datetime import datetime, timezone

from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from myapi.cruds.crud_examination import create_examination, get_examination_by_id, update_examination, delete_examination
from myapi.cruds.crud_patient import create_patient


class TestExaminationMethods(TestCase):
    
    def test_create_examination_valid(self):
        pat = create_patient("Martina", "Pletz", "martina.pletz@fhooe.at", "martina_password")
        date = datetime.now(timezone.utc)
        type = "P"
        ex = create_examination(date, pat, type)
        self.assertEqual(ex.pat, pat)
        self.assertEqual(ex.date, date)
        self.assertEqual(ex.type, type)

    def test_get_examination_valid_id(self):
        pat1 = create_patient("David", "Derntl", "david.derntl@fhooe.at", "david_password")
        date = datetime.now(timezone.utc)
        type = "I"
        ex1 = create_examination(date, pat1, type)
        ex2 = get_examination_by_id(ex1.exID)
        self.assertEqual(ex1.date.replace(tzinfo=None), ex2.date.replace(tzinfo=None))
        self.assertEqual(ex1.pat, ex2.pat)
        self.assertEqual(ex1.type, ex2.type)

    def test_update_examination_valid(self):
        patOld = create_patient("Nico", "Pointner", "nico.pointner@fhooe.at", "nico_password")
        patNew = create_patient("Eva", "Schoissengeier", "eva.schoissengeier@fhooe.at", "eva_password")
        date = datetime.now(timezone.utc)
        type = "P"
        exOld = create_examination(date, patOld, type)
        exNew = update_examination(exOld.exID, date, patNew, type)
        self.assertEqual(exNew.pat, patNew)

    def test_delete_examination_valid(self):
        pat = create_patient("Elisabeth", "Mayrhuber", "elisabeth.mayrhuber@fhooe.at", "elisabeth_password")
        date = datetime.now(timezone.utc)
        type = "I"
        ex = create_examination(date, pat, type)
        delete_examination(ex.exID)
        with self.assertRaises(ObjectDoesNotExist):
            get_examination_by_id(ex.exID)

    def test_delete_examination_invalid(self):
        with self.assertRaises(ObjectDoesNotExist):
            delete_examination(-1)
