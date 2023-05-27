from unittest import main, TestCase

from integer_to_roman import Solution


class AddTwoNumbersTest(TestCase):

    def test_add_two_numbers(self):
        test_data = [
            (58, "LVIII"),
            (1992, "MCMXCII")
        ]

        for number, expected_result in test_data:
            with self.subTest(number=number, expected_result=expected_result):
                result = Solution().intToRoman(number)
                self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
