from unittest import main, TestCase

from numbers_to_letters import Solution


class AddTwoNumbersTest(TestCase):

    def test_add_two_numbers(self):
        test_data = [
            ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
            ("", []),
            ("2", ["a", "b", "c"])
        ]

        for numbers, expected_result in test_data:
            with self.subTest(numbers=numbers, expected_result=expected_result):
                result = Solution().letterCombinations(numbers)
                self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
