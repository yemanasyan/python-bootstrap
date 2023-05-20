from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other) -> bool:
        if self is None and other is None:
            return True

        if self is None or other is None:
            return False

        return self.val == other.val and ((self.next is None and other.next is None) or (self.next == other.next))

    def __ne__(self, other):
        return not self.__eq__(self, other)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head

        # jump n positions forward
        for index in range(n):
            fast = fast.next if fast is not None else None

        # this covers the following cases:
        # 1. head = [1], n = 1 => []
        # 2. head = [1,2], n = 2 => [2]
        if not fast:
            return head.next

        # when fast reaches to the end the slow will be at position n from end as fast initially was n positions forward
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head


class Solution1:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head, _ = self._recursive_helper(head, n)
        return head

    def _recursive_helper(self, head: Optional[ListNode], n: int) -> (Optional[ListNode], int):
        if head == None:
            return None, 0
        else:
            chain, location = self._recursive_helper(head.next, n)
            location += 1
            if location == n:
                return chain, location
            else:
                return ListNode(head.val, chain), location

class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        iterator = head
        while iterator is not None:
            length += 1
            iterator = iterator.next

        remove_head_number = length - n
        return self._remove_nth_from_beginning(head, remove_head_number)

    def _remove_nth_from_beginning(self, head: Optional[ListNode], n: int):
        if head is None:
            return None
        elif n == 0:
            return head.next
        else:
            head.next = self._remove_nth_from_beginning(head.next, n - 1)
            return head
