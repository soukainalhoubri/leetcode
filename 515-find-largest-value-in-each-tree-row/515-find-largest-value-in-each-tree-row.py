# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result=[]
        q=deque()
        q.append(root)
        while q:
            level_length=len(q)
            level_max=-2**31
            for i in range(level_length):
                current=q.popleft()
                level_max=max(level_max,current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            result.append(level_max)
        return result
                