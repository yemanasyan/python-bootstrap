from unittest import main, TestCase

from container_with_most_water import Solution


class AddTwoNumbersTest(TestCase):

    def test_add_two_numbers(self):
        test_data = [
            ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
            ([1, 1], 1)
        ]

        for height, expected_result in test_data:
            with self.subTest(height=height, expected_result=expected_result):
                self.assertEqual(expected_result, Solution().maxArea(height))


if __name__ == "__main__":
    main()
