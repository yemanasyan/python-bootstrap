import unittest
from src.solution.longest_palindromic_substring import Solution


class MyTestCase(unittest.TestCase):
    def test_longest_palindrome(self):
        test_data = [
            ("babad", "bab"),
            ("cbbd", "bb"),
            ("abcdeffedcba", "abcdeffedcba"),
            ("abcdefedcba", "abcdefedcba")
        ]

        for input_string, expected_result in test_data:
            with self.subTest(input_string=input_string, expected_result=expected_result):
                result = Solution().longestPalindrome(input_string)
                self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
