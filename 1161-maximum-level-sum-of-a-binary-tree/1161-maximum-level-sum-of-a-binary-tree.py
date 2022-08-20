# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append(root)
        max_sum=-float('inf')
        current_depth=0
        level=0
        while q:
            current_depth+=1
            level_length=len(q)
            current_level=[]
            for _ in range(level_length):
                current=q.popleft()
                current_level.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            if sum(current_level)>max_sum:
                max_sum=sum(current_level)
                level=current_depth
        return level
                