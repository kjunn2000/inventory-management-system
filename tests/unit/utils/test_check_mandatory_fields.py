import unittest

from app.utils.app_error import MissingMandatoryFieldError
from app.utils.request_validation_utils import check_mandatory_fields


class TestCheckMandatoryFields(unittest.TestCase):

    def test_all_fields_present_and_not_empty(self):
        request = {
            "name": "short",
            "category": "cloth",
            "price": "16.22"
        }
        mandatory_fields = ["name", "category", "price"]

        self.assertTrue(check_mandatory_fields(request, mandatory_fields))

    def test_missing_field(self):
        request = {
            "category": "cloth",
            "price": "16.22"
        }
        mandatory_fields = ["name", "category", "price"]

        with self.assertRaises(MissingMandatoryFieldError) as context:
            check_mandatory_fields(request, mandatory_fields)

        self.assertEqual(str(context.exception), "Missing or empty value in mandatory field: name")

    def test_empty_field(self):
        request = {
            "name": "",
            "category": "cloth",
            "price": "16.22"
        }
        mandatory_fields = ["name", "category", "price"]

        with self.assertRaises(MissingMandatoryFieldError) as context:
            check_mandatory_fields(request, mandatory_fields)

        self.assertEqual(str(context.exception), "Missing or empty value in mandatory field: name")

    def test_null_field(self):
        request = {
            "name": None,
            "category": "cloth",
            "price": "16.22"
        }
        mandatory_fields = ["name", "category", "price"]

        with self.assertRaises(MissingMandatoryFieldError) as context:
            check_mandatory_fields(request, mandatory_fields)

        self.assertEqual(str(context.exception), "Missing or empty value in mandatory field: name")

    def test_empty_request(self):
        request = {}
        mandatory_fields = ["name", "category", "price"]

        with self.assertRaises(MissingMandatoryFieldError) as context:
            check_mandatory_fields(request, mandatory_fields)

        self.assertEqual(str(context.exception), "Missing or empty value in mandatory field: name")