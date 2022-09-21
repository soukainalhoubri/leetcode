# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #[1,2,3,4,5]
        #2
        current=head
        length=0
        while current:
            length+=1
            current=current.next
        current, previous = head, None#current=1,previous=None
        iteration=1
        while iteration<=(length//k):
            iteration+=1
            last_node_of_previous_part = previous#None
            last_node_of_sub_list = current#1
            next = None
            #start reversing for every K elements
            index = 0
            #what matters here is the number of items to reverse, we can start indexing from 0 and use i<k, or start indexing from 1, and end at i<=k
            while current and index < k:  # index=1, current = 2,k=2
                next = current.next# 2
                current.next = previous# [1] [2,3,4,5]
                previous = current#previous=1
                current = next#current=2
                index += 1
            #connect with the previous part
            if last_node_of_previous_part:
                last_node_of_previous_part.next = previous
            else:
                head = previous
            last_node_of_sub_list.next = current
            if not current :
                break
            previous = last_node_of_sub_list
            
        return head
        