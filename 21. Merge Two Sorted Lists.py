class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def mergeTwoLists(list1, list2):
    merged=None
    while(list1!=None and list2!=None):
       if(list1.val>=list2.val):
        merged.val=list2.val
        merged.next=list2.next
        list2=list2.next
       else:
        merged.val=list1.val
        merged.next=list1.next
        list1=list1.next
    if(list1!=None):
     merged.next=list1
    elif list2!=None:
     merged.next=list2
    return merged

print(e)
if:

       