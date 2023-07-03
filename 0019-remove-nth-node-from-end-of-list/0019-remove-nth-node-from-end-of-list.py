# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        base = ListNode(next=head)
        
        def dfs(node):
            if node is None:
                return 0

            next_idx = dfs(node.next)
            if next_idx == n:
                node.next = node.next.next
            return next_idx + 1
        dfs(base)

        return base.next
