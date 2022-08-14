# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
def check_symmetric(level):
    array=[]
    for node in level:
        if node:
            array.append(node.val)
        else:
            array.append(None)
    print(array)
    return array==array[::-1]
    
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q=deque()
        q.append(root)
        while q:
            level_length=len(q)
            level=q
            q=[]
            if not check_symmetric(level):
                return False
            for node in level:
                if node:
                    q.append(node.left)
                    q.append(node.right)
        return True