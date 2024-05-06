from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from myapi.cruds.crud_patient import create_patient, get_patient_by_id, update_patient, delete_patient


class TestPatientMethods(TestCase):
    def test_create_patient_def_valid(self):
        pat = create_patient("", "", "")
        self.assertEqual(pat.firstName, "John")
        self.assertEqual(pat.lastName, "Doe")
        self.assertEqual(pat.email, "unknown")

    def test_create_patient_fn_ln_valid(self):
        firstName = "Nico"
        lastName = "Pointner"
        pat = create_patient(firstName, lastName, "")
        self.assertEqual(pat.firstName, firstName)
        self.assertEqual(pat.lastName, lastName)

    def test_create_patient_mail_valid(self):
        email = "nico.pointner@gmail.com"
        pat = create_patient("", "", email)
        self.assertEqual(pat.firstName, "John")
        self.assertEqual(pat.lastName, "Doe")
        self.assertEqual(pat.email, email)

    def test_create_patient_fn_ln_mail_valid(self):
        firstName = "Nico"
        lastName = "Pointner"
        email = "nico.pointner@gmail.com"
        pat = create_patient(firstName, lastName, email)
        self.assertEqual(pat.firstName, firstName)
        self.assertEqual(pat.lastName, lastName)
        self.assertEqual(pat.email, email)

    def test_get_patient_valid_id(self):
        pat1 = create_patient("Martina", "Pletz")
        pat2 = get_patient_by_id(pat1.patID)
        self.assertEqual(pat1.firstName, pat2.firstName)
        self.assertEqual(pat1.lastName, pat2.lastName)

    def test_get_patient_invalid_id(self):
        with self.assertRaises(ObjectDoesNotExist):
            get_patient_by_id(-1)

    def test_update_patient_valid(self):
        patOld = create_patient("David", "Derntl")
        patNew = update_patient(patOld.patID, "Davina", "Derntl")
        self.assertEqual(patNew.firstName, "Davina")
        self.assertEqual(patNew.lastName, "Derntl")

    def test_delete_patient_valid(self):
        pat = create_patient("Elisabeth", "Mayrhuber")
        patID = pat.patID
        delete_patient(patID)
        with self.assertRaises(ObjectDoesNotExist):
            get_patient_by_id(patID)

    def test_delete_patient_invalid(self):
        with self.assertRaises(ObjectDoesNotExist):
            delete_patient(-1)
