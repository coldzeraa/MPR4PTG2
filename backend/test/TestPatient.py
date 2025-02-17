from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from myapi.cruds.crud_patient import create_patient, get_patient_by_id, update_patient, delete_patient


class TestPatientMethods(TestCase):
    def test_create_patient_def_valid(self):
        pat = create_patient("Nico", "Pointner", "nico.pointner@fhooe.at", "nico_password")
        self.assertEqual(pat.firstName, "Nico")
        self.assertEqual(pat.lastName, "Pointner")
        self.assertEqual(pat.email, "nico.pointner@fhooe.at")
        self.assertEqual(pat.password, "nico_password")

    def test_get_patient_valid_id(self):
        pat1 = create_patient("Martina", "Pletz", "martina.pletz@fhooe.at", "martina_password")
        pat2 = get_patient_by_id(pat1.patID)
        self.assertEqual(pat1.firstName, pat2.firstName)
        self.assertEqual(pat1.lastName, pat2.lastName)
        self.assertEqual(pat1.email, pat2.email)
        self.assertEqual(pat1.password, pat2.password)

    def test_get_patient_invalid_id(self):
        with self.assertRaises(ObjectDoesNotExist):
            get_patient_by_id(-1)

    def test_update_patient_valid(self):
        patOld = create_patient("David", "Derntl", "david.derntl@fhooe.at", "david_password")
        patNew = update_patient(patOld.patID, "Davina", "Derntl", "david_password")
        self.assertEqual(patNew.firstName, "Davina")
        self.assertEqual(patNew.lastName, "Derntl")
        self.assertEqual(patNew.password, "david_password")

    def test_delete_patient_valid(self):
        pat = create_patient("Elisabeth", "Mayrhuber", "elisabeth.mayrhuber@fhooe.at", "elisabeth_password")
        patID = pat.patID
        delete_patient(patID)
        with self.assertRaises(ObjectDoesNotExist):
            get_patient_by_id(patID)

    def test_delete_patient_invalid(self):
        with self.assertRaises(ObjectDoesNotExist):
            delete_patient(-1)
