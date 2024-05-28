import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from myapi.cruds.crud_patient import create_patient
import myapi.db.ExaminationService as EXS



class TestPointMethods(TestCase):
    def test_store_examination_valid(self):
        pat = create_patient("Martina", "Pletz")
        date = datetime.date.today()
        ex = EXS.ExaminationService.store(pat)
        self.assertEqual(ex.pat, pat)
        self.assertEqual(ex.date, date)

    def test_store_examination_valid_id(self):
        pat1 = create_patient("David", "Derntl")
        ex1 = EXS.ExaminationService.store(pat1)
        ex2 = EXS.ExaminationService.get(ex1.exID)
        self.assertEqual(ex1.date, ex2.date)
        self.assertEqual(ex1.pat, ex2.pat)

    def test_update_examination_valid(self):
        patOld = create_patient("Nico", "Pointner")
        patNew = create_patient("Eva", "Schoissengeier")
        date = datetime.date.today()
        exOld = EXS.ExaminationService.store(patOld)
        exNew = EXS.ExaminationService.update(exOld.exID, date, patNew)
        self.assertEqual(exNew.pat, patNew)

    def test_delete_examination_valid(self):
        pat = create_patient("Elisabeth", "Mayrhuber")
        ex = EXS.ExaminationService.store(pat)
        EXS.ExaminationService.delete(ex.exID)
        with self.assertRaises(ObjectDoesNotExist):
            EXS.ExaminationService.get(ex.exID)

    def test_delete_examination_invalid(self):
        with self.assertRaises(ObjectDoesNotExist):
            EXS.ExaminationService.delete(-1)
