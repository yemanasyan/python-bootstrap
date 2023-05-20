from unittest import TestCase
from src.solution.pairs_sum_divisible import Solution

class PairsSumDivisibleTest(TestCase):

    def test_count_divisible_pairs(self):
        test_data = [
            ([2, 2, 1, 7, 5, 3], 4, 5),
            ([5, 9, 36, 74, 52, 31, 42], 3, 7)
        ]

        for nums, divider, expected_result in test_data:
            with self.subTest(nums=nums, divider=divider, expected_result=expected_result):
                self.assertEqual(expected_result, Solution().count_divisible_pairs(nums, divider))