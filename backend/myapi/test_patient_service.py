from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from db.PatientService import PatientService as PatS


class TestPatientServiceMethods(TestCase):
    def test_get_all_patients(self):
        patientsCorr = [
            PatS.store("Martina", "Pletz"),
            PatS.store("Nico", "Pointner"),
            PatS.store("David", "Derntl"),
            PatS.store("Alexandra", "Denk")
        ]
        patientsRes = PatS.get_all()
        self.assertEqual(patientsCorr, patientsRes)

    def test_store_patient_def_valid(self):
        pat = PatS.store("", "", "")
        self.assertEqual(pat.firstName, "John")
        self.assertEqual(pat.lastName, "Doe")
        self.assertEqual(pat.email, "unknown")

    def test_store_patient_fn_ln_valid(self):
        firstName = "Nico"
        lastName = "Pointner"
        pat = PatS.store(firstName, lastName, "")
        self.assertEqual(pat.firstName, firstName)
        self.assertEqual(pat.lastName, lastName)

    def test_store_patient_mail_valid(self):
        email = "nico.pointner@gmail.com"
        pat = PatS.store("", "", email)
        self.assertEqual(pat.firstName, "John")
        self.assertEqual(pat.lastName, "Doe")
        self.assertEqual(pat.email, email)

    def test_store_patient_fn_ln_mail_valid(self):
        firstName = "Nico"
        lastName = "Pointner"
        email = "nico.pointner@gmail.com"
        pat = PatS.store(firstName, lastName, email)
        self.assertEqual(pat.firstName, firstName)
        self.assertEqual(pat.lastName, lastName)
        self.assertEqual(pat.email, email)

    def test_get_patient_valid_id(self):
        pat1 = PatS.store("Martina", "Pletz")
        pat2 = PatS.get(pat1.patID)
        self.assertEqual(pat1.firstName, pat2.firstName)
        self.assertEqual(pat1.lastName, pat2.lastName)

    def test_get_patient_invalid_id(self):
        with self.assertRaises(ObjectDoesNotExist):
            PatS.get(-1)

    def test_update_point_valid(self):
        patOld = PatS.store("David", "Derntl")
        patNew = PatS.update(patOld.patID, "Davina", "Derntl")
        self.assertEqual(patNew.firstName, "Davina")
        self.assertEqual(patNew.lastName, "Derntl")

    def test_delete_patient_valid(self):
        pat = PatS.store("Elisabeth", "Mayrhuber")
        patID = pat.patID
        PatS.delete(patID)
        with self.assertRaises(ObjectDoesNotExist):
            PatS.delete(patID)

    def test_delete_patient_invalid(self):
        with self.assertRaises(ObjectDoesNotExist):
            PatS.delete(-1)
