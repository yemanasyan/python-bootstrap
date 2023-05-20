from unittest import main
from unittest import TestCase
from src.solution.three_sum import Solution


class ThreeSumTest(TestCase):

    def test_three_sum_1(self):
        test_data = [
            ([1, 1, 0, -1, 10, 20, -30, -1, 2, 0, 0, 0], [[-30, 10, 20], [-1, -1, 2], [-1, 0, 1], [0, 0, 0]]),
            ([77, -20, 40, 30, 56], []),
            ([77, -20, 40, 30, 56, -57, 0, -56, -77, 37, 20], [[-77, 0, 77], [-77, 37, 40], [-57, -20, 77], [-57, 20, 37], [-56, 0, 56], [-20, 0, 20]])
        ]

        for input_numbers, expected_result in test_data:
            with self.subTest(input_numbers=input_numbers, expected_result=expected_result):
                self.assertEqual(sorted(expected_result), sorted(Solution().threeSum(input_numbers)))

    def test_three_sum_2(self):
        test_data = [
            ([1, 1, 0, -1, 10, 20, -30, -1, 2, 0, 0, 0], [[-30, 10, 20], [-1, -1, 2], [-1, 0, 1], [0, 0, 0]]),
            ([77, -20, 40, 30, 56], []),
            ([77, -20, 40, 30, 56, -57, 0, -56, -77, 37, 20], [[-77, 0, 77], [-77, 37, 40], [-57, -20, 77], [-57, 20, 37], [-56, 0, 56], [-20, 0, 20]])
        ]

        for input_numbers, expected_result in test_data:
            with self.subTest(input_numbers=input_numbers, expected_result=expected_result):
                self.assertEqual(sorted(expected_result), sorted(Solution().threeSum2(input_numbers)))

if __name__ == "__main__":
    main()