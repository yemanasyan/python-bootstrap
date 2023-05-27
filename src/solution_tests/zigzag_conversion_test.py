from unittest import TestCase, main
from src.solution.zigzag_conversion import Solution
from zigzag_conversion import Solution1


class ZigzagConversionTest(TestCase):

    def test_conversion(self):
        test_data = [
            ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
            ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
            ("ABCD", 1, "ABCD")
        ]

        for input_string, row_numbers, expected_result in test_data:
            with self.subTest(input_string=input_string, row_numbers=row_numbers, expected_result=expected_result):
                result = Solution().convert(input_string, row_numbers)
                self.assertEqual(expected_result, result)


    def test_conversion_1(self):
        test_data = [
            ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
            ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
            ("ABCD", 1, "ABCD")
        ]

        for input_string, row_numbers, expected_result in test_data:
            with self.subTest(input_string=input_string, row_numbers=row_numbers, expected_result=expected_result):
                result = Solution1().convert(input_string, row_numbers)
                self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
