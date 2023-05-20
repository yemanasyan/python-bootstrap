from unittest import main, TestCase
from src.solution.longest_substring_length import Solution, Solution1

class LongestSubstringLengthTest(TestCase):

    def test_length_of_longest_substring(self):
        test_data = [
            ("abcdefgh", 8),
            ("abcbfghlmn", 8),
            ("aaaaaaaaa", 1),
            ("somethingnew", 9)
        ]

        for input_string, expected_result in test_data:
            with self.subTest(input_string=input_string, expected_result=expected_result):
                self.assertEqual(expected_result, Solution().lengthOfLongestSubstring(input_string))

    def test_length_of_longest_substring_solution1(self):
        test_data = [
            ("abcdefgh", 8),
            ("abcbfghlmn", 8),
            ("aaaaaaaaa", 1),
            ("somethingnew", 9)
        ]

        for input_string, expected_result in test_data:
            with self.subTest(input_string=input_string, expected_result=expected_result):
                self.assertEqual(expected_result, Solution1().lengthOfLongestSubstring(input_string))

if __name__ == "__main__":
    main()