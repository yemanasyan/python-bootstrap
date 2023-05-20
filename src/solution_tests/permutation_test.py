import unittest
from unittest import TestCase

from src.solution.permutation import permutation


class PermutationTest(TestCase):

    def test_permutation(self):
        test_parameters = [("string1", "string2", False), ("dog", "god", True), ("hello", "ollhe", True)]
        for value1, value2, expected_result in test_parameters:
            with self.subTest(first_string=value1, second_string=value2, expected_result=expected_result):
                self.assertEqual(expected_result, permutation(value1, value2))

if __name__ == "__main__":
    unittest.main()