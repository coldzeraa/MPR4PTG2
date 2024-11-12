from datetime import datetime, timezone

from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from myapi.cruds.crud_patient import create_patient
from myapi.db.ExaminationService import ExaminationService as EXS



class TestPointMethods(TestCase):
    def test_store_examination_valid(self):
        pat = create_patient("Martina", "Pletz", "martina.pletz@fhooe.at", "martina_password")
        date = datetime.now(timezone.utc)
        type = "P"
        ex = EXS.store(pat, type, date)
        self.assertEqual(ex.pat, pat)
        self.assertEqual(ex.date, date)
        self.assertEqual(ex.type, type)

    def test_store_examination_valid_id(self):
        pat1 = create_patient("David", "Derntl", "david.derntl@fhooe.at", "david_password")
        date = datetime.now(timezone.utc)
        type = "P"
        ex1 = EXS.store(pat1, type, date)
        ex2 = EXS.get(ex1.exID)
        self.assertEqual(ex1.date, ex2.date)        
        self.assertEqual(ex1.pat, ex2.pat)
        self.assertEqual(ex1.type, ex2.type)

    def test_update_examination_valid(self):
        patOld = create_patient("Nico", "Pointner", "nico.pointi@fhooe.at", "nico_password")
        patNew = create_patient("Eva", "Schoissengeier", "eva.schoissengeier@fhooe.at", "eva_password")
        date = datetime.now(timezone.utc)
        type = "P"
        exOld = EXS.store(patOld, type, date)
        exNew = EXS.update(exOld.exID, date, patNew, type)
        self.assertEqual(exNew.pat, patNew)

    def test_delete_examination_valid(self):
        pat = create_patient("Elisabeth", "Mayrhuber", "elisabeth.mayrhuber@fhooe.at", "elisabeth_password")
        date = datetime.now(timezone.utc)
        type = "I"
        ex = EXS.store(pat, type, date)
        EXS.delete(ex.exID)
        with self.assertRaises(ObjectDoesNotExist):
            EXS.get(ex.exID)

    def test_delete_examination_invalid(self):
        with self.assertRaises(ObjectDoesNotExist):
            EXS.delete(-1)
