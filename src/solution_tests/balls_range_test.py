import unittest

from balls_range import Solution


class BallsRangeTestCase(unittest.TestCase):
    def test_min_moves(self):
        test_data = [
            ([6, 4, 1, 7, 10], 2),
            ([25], 0),
            ([25, 23], 1),
            ([25, 24], 0),
            ([2, 5, 4], 1),
            (
                [5, 73, 96, 228, 963, 694, 485, 700, 430, 886, 60, 291, 829, 27, 185, 667, 659, 879, 167, 603, 80, 677,
                 837, 693, 802, 109, 722, 953, 423, 163, 821, 63, 650, 927, 406, 67, 935, 328, 114, 403, 281, 811, 778,
                 789, 685, 556, 538, 377, 479, 547], 43
            )
        ]

        solution = Solution()
        for balls, min_moves in test_data:
            with self.subTest(balls=balls, min_moves=min_moves):
                result = solution.min_moves(balls)
                self.assertEqual(min_moves, result)


if __name__ == '__main__':
    unittest.main()
