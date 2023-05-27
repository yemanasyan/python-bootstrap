from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        last_pointer = ListNode()
        swapped_head = last_pointer
        fast_pointer = head.next
        slow_pointer = head

        while fast_pointer is not None:
            second_node = ListNode(slow_pointer.val)
            last_pointer.next = ListNode(fast_pointer.val, second_node)
            last_pointer = second_node

            slow_pointer = fast_pointer.next
            fast_pointer = slow_pointer.next if slow_pointer is not None else None

        if slow_pointer is not None:
            last_pointer.next = ListNode(slow_pointer.val)

        return swapped_head.next