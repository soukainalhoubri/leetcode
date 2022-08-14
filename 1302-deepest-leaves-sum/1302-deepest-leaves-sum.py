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
            _sum=0
            level=len(q)
            for i in range(level):
                current=q.popleft()
                _sum+=current.val
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
        return _sum
        