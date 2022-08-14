# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
def get_grand_sum(root):
    answer=0
    q=deque()
    q.append(root)
    depth=0
    while q:
        depth+=1
        level=q
        q=deque()
        for current in level:
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        
        if depth==3 and level:
            print(level)
            for node in level:
                answer+=node.val
    return answer
            
        
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        #what is in common between the grandparents and grand-children: 
        #the parity of their level
        
        q=deque()
        q.append(root)
        answer=0
        while q:
            current=q.popleft()
            if current.val%2==0:
                answer+=get_grand_sum(current)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            
            
        return answer