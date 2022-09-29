# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append(root)
        while q:
            current_level_length=len(q)
            current_level=[]
            for _ in range(current_level_length):
                current=q.popleft()
                current_level.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
        return sum(current_level)
                
                