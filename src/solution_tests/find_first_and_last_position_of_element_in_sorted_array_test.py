import unittest

from find_first_and_last_position_of_element_in_sorted_array import Solution


class FindFirstAndLastPositionOfElementInSortedArrayTestCase(unittest.TestCase):
    def test_search_range(self):
        test_data = [
            ([5, 7, 7, 8, 8, 10], 7, [1, 2]),
            ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
            ([5, 7, 7, 8, 8, 10], 10, [5, 5]),
            ([5, 7, 7, 8, 8, 10], 1, [-1, -1]),
            ([5, 7, 7, 8, 8, 10, 10, 10, 10], 10, [5, 8]),
        ]

        for input_array, target, expected_range in test_data:
            with self.subTest(input_array=input_array, target=target, expected_range=expected_range):
                solution = Solution()
                result_range = solution.searchRange(input_array, target)
                self.assertEqual(expected_range, result_range)


if __name__ == '__main__':
    unittest.main()
