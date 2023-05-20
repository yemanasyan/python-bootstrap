from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other) -> bool:
        return self.val == other.val and ((self.next is None and other.next is None) or (self.next == other.next))

    def __ne__(self, other):
        return not self.__eq__(self, other)


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return_node = ListNode()
        current_node = return_node
        pass_value = 0

        while current_node is not None:
            value1 = l1.val if l1 is not None else 0
            value2 = l2.val if l2 is not None else 0
            summary = value1 + value2 + pass_value
            pass_value = summary // 10
            current_node.val = summary % 10
            current_node.next = ListNode() if (l1 is not None and l1.next is not None) or \
                                              (l2 is not None and l2.next is not None) or pass_value > 0 else None
            current_node = current_node.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return return_node


class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], pass_value: int = 0) -> Optional[ListNode]:
        value1 = l1.val if l1 is not None else 0
        value2 = l2.val if l2 is not None else 0
        summary = value1 + value2 + pass_value
        pass_value = summary // 10
        current_node_value = summary % 10

        next_value = None
        if (l1 is not None and l1.next is not None) or (l2 is not None and l2.next is not None) or pass_value > 0:
            next_l1 = l1.next if l1 is not None else None
            next_l2 = l2.next if l2 is not None else None
            next_value = self.addTwoNumbers(next_l1, next_l2, pass_value)

        return ListNode(current_node_value, next_value)


class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            raise Exception(f"Provided values can't be None. l1: {l1}, l2: {l2}")

        number1 = self.getNumber(l1)
        number2 = self.getNumber(l2)

        sum = number1 + number2

        return self.getListNode(sum)

    def getNumber(self, l: ListNode) -> int:
        if l.next is not None:
            return self.getNumber(l.next) * 10 + l.val
        return l.val

    def getListNode(self, number: int) -> ListNode:
        if number // 10 == 0:
            return ListNode(number % 10)

        return ListNode(number % 10, self.getListNode(number // 10))
