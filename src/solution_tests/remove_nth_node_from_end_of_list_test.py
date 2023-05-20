from unittest import TestCase
from src.solution.remove_nth_node_from_end_of_list import Solution, Solution1, Solution2, ListNode
from typing import Optional

class RemoveNthNodeFromEndOfListTest(TestCase):

    def test_remove_nth_from_end(self):
        test_data = [
            ([1,2,3,4,5], 2, [1,2,3,5]),
            ([1], 1, []),
            ([1,2], 1, [1])
        ]

        for input_numbers, node_index_from_end, output_numbers in test_data:
            with self.subTest(input_numbers=input_numbers, node_index_from_end=node_index_from_end,
                              output_numbers=output_numbers):
                input_list = self.get_list_node(input_numbers)
                output_list = self.get_list_node(output_numbers)
                result = Solution().removeNthFromEnd(input_list, node_index_from_end)
                self.assertEqual(output_list, result)

    def test_remove_nth_from_end_solution_1(self):
        test_data = [
            ([1,2,3,4,5], 2, [1,2,3,5]),
            ([1], 1, []),
            ([1,2], 1, [1])
        ]

        for input_numbers, node_index_from_end, output_numbers in test_data:
            with self.subTest(input_numbers=input_numbers, node_index_from_end=node_index_from_end,
                              output_numbers=output_numbers):
                input_list = self.get_list_node(input_numbers)
                output_list = self.get_list_node(output_numbers)
                result = Solution1().removeNthFromEnd(input_list, node_index_from_end)
                self.assertEqual(output_list, result)
    def test_remove_nth_from_end_solution_2(self):
        test_data = [
            ([1,2,3,4,5], 2, [1,2,3,5]),
            ([1], 1, []),
            ([1,2], 1, [1])
        ]

        for input_numbers, node_index_from_end, output_numbers in test_data:
            with self.subTest(input_numbers=input_numbers, node_index_from_end=node_index_from_end,
                              output_numbers=output_numbers):
                input_list = self.get_list_node(input_numbers)
                output_list = self.get_list_node(output_numbers)
                result = Solution2().removeNthFromEnd(input_list, node_index_from_end)
                self.assertEqual(output_list, result)

    def get_list_node(self, numbers: [int]) -> Optional[ListNode]:
        if len(numbers) == 0:
            return None
        else:
            number = numbers.pop(0)
            next_node = self.get_list_node(numbers)
            return ListNode(number, next_node)
