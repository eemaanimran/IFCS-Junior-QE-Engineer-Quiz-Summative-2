import unittest # Automated unit tests
from validation import validate_name, validate_answer, validate_multiple_choice_answer # Input validators

class TestValidateAnswer(unittest.TestCase):
    """
    Automated unit tests for validation module. 
    These tests verify that validation functions return the expected outputs for valid and invalid user inputs.
    """
    def test_valid_name(self):
        result = validate_name("John")
        self.assertEqual(result, True)

    def test_empty_name(self):
        result = validate_name("")
        self.assertEqual(result, "Name Field cannot be left empty")

    def test_valid_manual_answer(self):
        result = validate_answer("API Testing")
        self.assertEqual(result, True)

    def test_empty_manual_answer(self):
        result = validate_answer("")
        self.assertEqual(result, "Answer Field cannot be left empty")

    def test_valid_multiple_choice_answer(self):
        result = validate_multiple_choice_answer("User Acceptance Testing")
        self.assertEqual(result, True)

    def test_empty_multiple_choice_answer(self):
        result = validate_multiple_choice_answer("Select an Answer")
        self.assertEqual(result, "Please Select an Answer")


if __name__ == "__main__":
     unittest.main()