import unittest

from src.solution.unique_chars import all_unique_chars_solution_1
from unique_chars import all_unique_chars_solution_2


class AllUniqueCharsTestCase(unittest.TestCase):
    def test_all_unique_chars_solution_1(self):
        value = "something"
        self.assertTrue(all_unique_chars_solution_1(value), f"Expected that {value} has all unique chars")

        value = "again"
        self.assertFalse(all_unique_chars_solution_1(value), f"Expected that {value} has all unique chars")

        value = "One more time"
        self.assertFalse(all_unique_chars_solution_1(value), f"Expected that {value} has all unique chars")

    def test_all_unique_chars_solution_2(self):
        test_case_value = [("something", True), ("again", False), ("A huge string", False)]
        for value, expected_result in test_case_value:
            with self.subTest(value=value, expected_result=expected_result):
                self.assertEqual(expected_result, all_unique_chars_solution_2(value))



if __name__ == '__main__':
    unittest.main()
