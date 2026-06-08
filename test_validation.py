import unittest
from validation import validate_name, validate_answer, validate_multiple_choice_answer

class TestValidateAnswer(unittest.TestCase):
    def test_valid_name(self):
        result = validate_name("John")
        self.assertEqual(result, True)

    def test_empty_name(self):
        result = validate_name("")
        self.assertEqual(result, "Name field cannot be left empty")

    def test_valid_manual_answer(self):
        result = validate_answer("")