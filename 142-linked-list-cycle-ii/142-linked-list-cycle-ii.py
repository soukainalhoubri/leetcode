# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #find the cycle
        #store all of the items in the cycle
        #I will iterate over the list again, once I meet an item which is in the cycle, I return it. That's what we're ooking for
        if not head or not head.next:
            return None
        slow,fast=head,head
        while slow and fast.next:
            fast=fast.next
            if not fast:
                return None
            fast=fast.next
            if not fast:
                return None
            slow=slow.next
            if slow==fast:
                break
        print("done with first loop")
        if not slow or not fast.next:
            return None
        cycle=set([slow])
        current=slow
        while slow.next!=current:
            slow=slow.next
            cycle.add(slow)
        print("done with second loop")
        current=head
        while current:
            if current in cycle:
                return current
            current=current.next
        print("done with third loop")