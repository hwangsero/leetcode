from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy_head = ListNode()
        node = dummy_head
        while l1 is not None or l2 is not None or carry > 0:
            next = ListNode()
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            sum = x + y + carry
            next.val = sum % 10
            carry = sum // 10
            node.next = next
            node = next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return dummy_head.next

