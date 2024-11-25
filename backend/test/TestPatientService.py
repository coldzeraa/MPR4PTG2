from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from myapi.db.PatientService import PatientService as PatS


class TestPatientServiceMethods(TestCase):
    def test_get_all_patients(self):
        patientsCorr = [
            PatS.store("Martina", "Pletz", "martina.pletz@fhooe.at", "martina_password"),
            PatS.store("Nico", "Pointner", "nico.pointner@fhooe.at", "nico_password"),
            PatS.store("David", "Derntl", "david.derntl@fhooe.at", "david_password"),
            PatS.store("Alexandra", "Denk", "alex.denk@fhooe.at", "alex_password")
        ]
        patientsRes = PatS.get_all()
        for index, patient in enumerate(patientsCorr):
            self.assertEqual(patient, patientsRes[index])

    def test_store_patient_def_valid(self):
        pat = PatS.store()
        self.assertEqual(pat.firstName, None)
        self.assertEqual(pat.lastName, None)
        self.assertEqual(pat.email, None)
        self.assertEqual(pat.password, None)

    def test_store_patient_fn_ln_mail_valid(self):
        firstName = "Nico"
        lastName = "Pointner"
        email = "nico.pointner@gmail.com"
        password = "nico_password"
        pat = PatS.store(firstName, lastName, email, password)
        self.assertEqual(pat.firstName, firstName)
        self.assertEqual(pat.lastName, lastName)
        self.assertEqual(pat.email, email)
        self.assertEqual(pat.password, password)

    def test_get_patient_invalid_id(self):
        with self.assertRaises(ObjectDoesNotExist):
            PatS.get(-1)

    def test_update_point_valid(self):
        patOld = PatS.store("David", "Derntl", "david.derntl@fhooe.at", "david_password")
        patNew = PatS.update(patOld.patID, "Davina", "Derntl", "david_password")
        self.assertEqual(patNew.firstName, "Davina")
        self.assertEqual(patNew.lastName, "Derntl")
        self.assertEqual(patNew.password, "david_password")

    def test_delete_patient_valid(self):
        pat = PatS.store("Elisabeth", "Mayrhuber", "elisabeth.mayrhuber@fhooe.at", "elisabeth_password")
        patID = pat.patID
        PatS.delete(patID)
        with self.assertRaises(ObjectDoesNotExist):
            PatS.delete(patID)

    def test_delete_patient_invalid(self):
        with self.assertRaises(ObjectDoesNotExist):
            PatS.delete(-1)
