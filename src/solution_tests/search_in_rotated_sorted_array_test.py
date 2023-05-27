import unittest

from search_in_rotated_sorted_array import Solution


class SearchInRotatedSortedArrayTestCase(unittest.TestCase):
    def test_search(self):
        test_data = [
            ([4, 5, 6, 7, 0, 1, 2], 0, 4),
            ([4, 5, 6, 7, 0, 1, 2], 3, -1),
            ([4, 5, 6, 7, 0, 1, 2], 4, 0),
            ([4, 5, 6, 7, 0, 1, 2], 5, 1),
            ([4, 5, 6, 7, 0, 1, 2], 2, 6),
            ([4, 5, -5, -4, -3, -2, -1], 5, 1),
        ]

        for input_array, target, expected_index in test_data:
            with self.subTest(input_array=input_array, target=target, expected_index=expected_index):
                solution = Solution()
                index = solution.search(input_array, target)
                self.assertEqual(expected_index, index)


if __name__ == '__main__':
    unittest.main()
