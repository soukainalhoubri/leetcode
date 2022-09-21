# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length=0
        current=head
        while current:
            length+=1
            current=current.next
        #we can get the legnth of , and only rotate using K%length
        def rotate_once(head):
            current,previous=head,None
            while current.next:
                previous=current
                current=current.next
            previous.next=None
            node=ListNode(current.val)
            node.next=head
            head=node
            return head
        i=0
        while i<(k%length):
            head=rotate_once(head)
            i+=1
        return head

            