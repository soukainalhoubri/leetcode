# Definition for singly-linked list.
#leetcode problem 2
#difficulty: medium


#the problem
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def make_int(node):
    i=0
    result=0
    while(node!=None):
        result+=node.val*10**i
        i+=1
        node=node.next
    return result
def tolist(n):
    node = ListNode(n % 10)
    if n > 9:
        node.next = tolist(n // 10)
    return node

def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    n=make_int(l1)+make_int(l2)
    L=tolist(n)
    return(L)