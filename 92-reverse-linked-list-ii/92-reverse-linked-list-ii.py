# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        #skip the first left-1 nodes while keeping track on previous node
        index=0
        current,previous=head,None
        while current and index<left-1:
            previous=current
            current=current.next
            index+=1
        
        last_node_of_left_part=previous
        last_node_of_sublist=current
        store_next=None
        index=0
        while current and index<right-left+1:#the number of nodes in the sublist
            store_next=current.next
            current.next = previous
            previous = current
            current = store_next
            index += 1
        if last_node_of_left_part:
            last_node_of_left_part.next=previous
        else:
            head=previous
        last_node_of_sublist.next=current
        return head
            
            