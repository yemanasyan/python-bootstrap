from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake_return_head = ListNode()
        current_node = fake_return_head
        while head is not None:
            duplicate_detected = False
            while head.next is not None and head.val == head.next.val:
                head = head.next
                duplicate_detected = True

            if not duplicate_detected:
                current_node.next = ListNode(head.val)
                current_node = current_node.next

            head = head.next

        return fake_return_head.next
