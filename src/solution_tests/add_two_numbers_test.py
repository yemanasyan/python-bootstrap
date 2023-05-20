from unittest import main, TestCase
from src.solution.add_two_numbers import ListNode, Solution, Solution1, Solution2

class AddTwoNumbersTest(TestCase):

    def test_add_two_numbers(self):
        test_data = [
            (self.get_list_node(111), self.get_list_node(222), self.get_list_node(333)),
            (self.get_list_node(999), self.get_list_node(111), self.get_list_node(1110)),
            (self.get_list_node(1), self.get_list_node(0), self.get_list_node(1)),
            (self.get_list_node(9), self.get_list_node(222), self.get_list_node(231)),
        ]

        for list_node1, list_node2, expected_result in test_data:
            with self.subTest(list_node1=list_node1,list_node2= list_node2, expected_result=expected_result):
                self.assertEqual(expected_result, Solution().addTwoNumbers(list_node1, list_node2))

    def test_add_two_numbers_solution1(self):
        test_data = [
            (self.get_list_node(111), self.get_list_node(222), self.get_list_node(333)),
            (self.get_list_node(999), self.get_list_node(111), self.get_list_node(1110)),
            (self.get_list_node(1), self.get_list_node(0), self.get_list_node(1)),
            (self.get_list_node(9), self.get_list_node(222), self.get_list_node(231)),
        ]

        for list_node1, list_node2, expected_result in test_data:
            with self.subTest(list_node1=list_node1,list_node2= list_node2, expected_result=expected_result):
                self.assertEqual(expected_result, Solution1().addTwoNumbers(list_node1, list_node2))

    def test_add_two_numbers_solution2(self):
        test_data = [
            # (self.get_list_node(111), self.get_list_node(222), self.get_list_node(333)),
            (self.get_list_node(999), self.get_list_node(111), self.get_list_node(1110)),
            # (self.get_list_node(1), self.get_list_node(0), self.get_list_node(1)),
            # (self.get_list_node(9), self.get_list_node(222), self.get_list_node(231)),
        ]

        for list_node1, list_node2, expected_result in test_data:
            with self.subTest(list_node1=list_node1,list_node2= list_node2, expected_result=expected_result):
                self.assertEqual(expected_result, Solution2().addTwoNumbers(list_node1, list_node2))

    def get_list_node(self, number: int) -> ListNode:
        next_value = None
        if number // 10 > 0:
            next_value = self.get_list_node(number // 10)

        return ListNode(number % 10, next_value)

if __name__ == "__main__":
    main()