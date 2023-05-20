import unittest
from src.solution.puzzle_game_min_obstacle_removal import Solution


class PuzzleGameMinObstacleRemoval(unittest.TestCase):
    def test_something(self):
        test_data = [
            ([
                ["." , "*", ".", "#"],
                ["*" , "*", "*", "#"],
                ["." , "*", "#", "#"],
                ["#" , "#", ".", "#"],
            ], 2),

            ([
                 ["." , "*", ".", "#"],
                 ["*" , "*", "*", "#"],
                 ["." , "*", "#", "#"],
                 ["." , ".", ".", "#"],
             ], 1),

            ([
                 ["." , "*", ".", "#"],
                 ["*" , "*", "*", "#"],
                 ["." , "*", ".", "#"],
                 ["." , ".", ".", "#"],
             ], 0),

            ([
                 ["." , "*", ".", "#"],
                 ["*" , "*", "*", "#"],
                 ["." , "*", ".", "#"],
                 ["." , "*", "#", "#"],
             ], 0),

            ([
                 ["." , "*", ".", "#"]
             ], 0)
        ]

        for input_matrix, expected_result in test_data:
            with self.subTest(input_matrix=input_matrix, expected_result=expected_result):
                result = Solution().remove(input_matrix)
                self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
