from unittest import main
from unittest import TestCase
from src.solution.three_sum_closest import Solution

class ThreeSumCloses(TestCase):

    def test_three_sum_closest(self):
        test_data = [
            ([-1,2,1,-4], 1, 2),
            ([0,0,0], 1, 0),
        ]

        for input_numbers, target, expected_result in test_data:
            with self.subTest(input_numbers=input_numbers, target=target, expected_result=expected_result):
                self.assertEqual(expected_result, Solution().threeSumClosest(input_numbers, target))

if __name__ == "__main__":
    main()