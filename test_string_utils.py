# test_string_utils.py

import unittest
from string_utils import reverse_string, is_palindrome

class TestStringUtils(unittest.TestCase):

    # ----------------------------------------------------
    # Tests for reverse_string function
    # ----------------------------------------------------

    def test_reverse_normal_string(self):
        """Test a normal, multi-character string reversal."""
        expected = "olleh"
        actual = reverse_string("hello")
        self.assertEqual(actual, expected)

    def test_reverse_empty_string(self):
        """Test handling of an empty string."""
        expected = ""
        actual = reverse_string("")
        self.assertEqual(actual, expected)

    def test_reverse_type_error(self):
        """Test that non-string input raises a TypeError."""
        # self.assertRaises is a key unittest assertion for exceptions
        with self.assertRaises(TypeError):
            reverse_string(12345)

    # ----------------------------------------------------
    # Tests for is_palindrome function
    # ----------------------------------------------------

    def test_is_palindrome_true(self):
        """Test a known palindrome (racecar)."""
        self.assertTrue(is_palindrome("racecar"))

    def test_is_palindrome_with_spaces_and_case(self):
        """Test a palindrome with spaces and mixed case (A man a plan)."""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_is_palindrome_false(self):
        """Test a known non-palindrome."""
        self.assertFalse(is_palindrome("testing"))