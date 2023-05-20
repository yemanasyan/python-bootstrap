from unittest import main
from unittest import TestCase

from src.solution.two_sum import Solution

class TwoSumTest(TestCase):

    def test_two_sum(self):
        test_data = [
            ([1, 20, 300, 4, 10, 50, 78, 44, 40, 20, 20], 60, [[10, 50], [20, 40]]),
            ([-10, 30, 20, 0, -40, 80, -60, 47, -27, 40, 60], 20, [[-60, 80], [-40, 60], [-27, 47], [-10, 30], [0, 20]]),
            ([-10, 30, 20, 0, -40, 80, -60, 47, -27, 40], 800, [])
        ]

        for input_array, summary, expected_result in test_data:
            with self.subTest(input_array=input_array, summary=summary, expected_result=expected_result):
                self.assertEqual(expected_result, Solution().twoSum(input_array, summary))

if __name__ == "__main__":
    main()