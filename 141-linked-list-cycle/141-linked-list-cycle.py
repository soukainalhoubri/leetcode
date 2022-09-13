# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow,fast=head,head.next
        if not fast:
            return False
        while slow:
            if fast==slow:
                return True
            fast=fast.next
            if fast==None:
                return False
            if fast==slow:
                return True
            fast=fast.next
            if fast==None:
                return False
            if fast==slow:
                return True
            slow=slow.next
        return False
                